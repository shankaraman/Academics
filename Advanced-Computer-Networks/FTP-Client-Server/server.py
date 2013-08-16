#!/usr/bin/python 
import sys
from socket import *
import subprocess
def bind_(host, port):
	st = socket(AF_INET, SOCK_STREAM)
	st.bind((host,port))
	st.listen(5)
	while 1:
		con, addr = st.accept()
		while 1:
		   try:
	    		cmd = con.recv(30)
			#print cmd
			if "lst" in cmd:
				pop = subprocess.Popen(['ls','-1'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
				
				data = pop.stdout.read()
				con.send(data)
		
			elif "get" in cmd:
				foo = cmd.split("get ")[1].split("\r")[0]
				try:	
					off = open(foo, 'r')
	                        	data = off.read()
					con.send("ok\r\n")
					con.send(str(off.tell())+"\r\n")
		                        con.send(data +"\r\n")

				except:
					con.send("wr\r\n")

			elif "put" in cmd:
				print "i am inside put()"
	                        foo = cmd.split("put ")[1].split("\r")[0]
				print "yeah i got your file name "
				#print repr(foo)
				o = open(foo,'wb')
				l = con.recv(1024).strip()
				con.settimeout(5)
				while (1):
					o.write(l)
					try:
                	        		l = con.recv(1024).strip()
					except:
						break

                                o.close()
			
			else:
				continue
		   		
		   except:
				continue		   
	con.close()
	st.close()

if __name__ == "__main__":
        server = "127.0.0.1"
        port = int(sys.argv[1])
        bind_(server, port)
	
