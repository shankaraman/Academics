# By Rowland Yu
signatures = {
'map_header' : 'rule map_header { \
strings: \
$hex = {00 00 ?? ?? 01 00 00 00 00 00 00 00 01 00 ?? ?? ?? ?? ?? ?? 70 00 00 00 02 00} \
condition: $hex }'
}
class apk_packer_find_dex(linux_common.AbstractLinuxCommand):

	"""Gather information about the dex Dump in Memory running in the system"""

	def __init__(self, config, *args, **kwargs):

		linux_common.AbstractLinuxCommand.__init__(self, config, *args, **kwargs)
		self._config.add_option('PID', short_option='p', default=None,
		help='Operate on a specifi c Android application Process ID',
		action='store', type='str')


	def calculate(self):

	""" Required: Runs YARA search to find hits """

		rules = yara.compile(sources = signatures)
		proc_maps = linux_proc_maps.linux_proc_maps(self._config).calculate()
		for task, vma in proc_maps:
		if not vma.vm_file:
			if vma.vm_start <= task.mm.start_brk and vma.vm_end >= task.mm.brk:
				continue
			elif vma.vm_start <= task.mm.start_stack and vma.vm_end >= task.mm.start_stack:
				continue
			elif vma.vm_end - vma.vm_start > 0x1000:
				proc_as = task.get_process_address_space()
				maxlen = vma.vm_end - vma.vm_start
				data = proc_as.zread(vma.vm_start, maxlen - 1)
				if data:
					for match in rules.match(data = data):
						for moffset, _name, _value in match.strings:
							(usize,) = struct.unpack('I', data[moffset - 4 : moffset])
							i = 0
							offset = moffset
							while i < usize:
								(maptype,) = struct.unpack('H', data[offset: offset+2])
								(mapoffset,) = struct.unpack('I', data[offset+8: offset+12])

								if maptype == 0x1000:
									yield task, vma, moffset - 4 - mapoffset, moffset
									break
								i += 1
								offset += 12

	def render_text(self, outfd, data):
		self.table_header(outfd, [(”Task”, ”10”),
		(”VM Start”, ”[addrpad]”),
		(”VM End”, ”[addrpad]”),
		(”Dex Offset”, ”[addr]”),
		(”Map Offset”, ”[addr]”)])
		
		for (task, vma, offset, moffset) in data:
		self.table_row(outfd, task.pid, vma.vm_start, vma.vm_end, offset, moffset - 4)
