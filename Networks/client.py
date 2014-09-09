#!/usr/bin/python 
import sys
from socket import *
asciii = """
MY FTP CLIENT
"""
def connect_(serv, port):
	st = socket(AF_INET, SOCK_STREAM)
	st.connect((serv, port))
	st.settimeout(3)
	print asciii
	data = ""
	while(1):
		io = raw_input(">>")
		print io
		if "lst" in io:
			st.send(io+"\r\n")
			data = st.recv(1024)
			print data
		elif "get" in io:
                        st.send(io+"\r\n")
			check = st.recv(4)
			print check
                        if "ok" in check:
	                        foo = io.split("get ")[1].split("\n")[0]
				print repr(foo)
				o = open(foo,'wb')
				size = int(st.recv(1024).split()[0].strip())
				print "file size :%d"%size
				l=st.recv(1024)
				while(1):
					o.write(l)
					try:
						l = st.recv(1024)
					except:
						break
				o.close()
			else:
				print "Error no such file\n"
		
		elif "put" in io:
				data = ""
	                        st.send(io+"\r\n")
                                foo = io.split("put ")[1].split("\r")[0]
                                print repr(foo)
                                off = open(foo, 'r')
                                data = off.read(1024)
	                  	while (data):
					st.send(data +"\r\n")
					data = off.read(1024)

				off.close()
		else:
                       print "error..\n" 
	 

if __name__ == "__main__":
	server = sys.argv[1]
	port = int(sys.argv[2])
	connect_(server, port)
