import SimpleXMLRPCServer
import os,sys
import hashlib

class PaperServer:

    def list(self):
        output = os.popen("ls files/").readlines()
        data = ' '.join(output)
        return data

    def server_receive_file(self,arg,author_name,paper_title):
        with open("files/"+str(paper_title),"wb") as handle:
            handle.write(arg.data)
            return True

server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost",8000))
server.register_instance(PaperServer())
server.serve_forever()
