import SimpleXMLRPCServer
import os,sys
import hashlib,random


# Removes the directory named files and creates a new directory named 'files'

os.system("rm -r files")
os.mkdir("files")

# Global Variables

session_list = []
dictionary = {}
count = 0 # Whether to update or add values to dictionary

class PaperServer:

"""    
    Lists the contents inside the "files" folder
    Returns the unique string with author name and title of a paper
"""
    def list(self):
        global count,dictionary,session_list
        output = os.popen("ls files/").readlines()
        data = ' '.join(output)
        return str("Author:"+dictionary.values()[0][0]+"\nTitle"+dictionary.values()[0][1]+"\nUnique id:"+str(dictionary.keys()).strip("[]''"))

"""
    # Stores the file under the "files" folder
    # Stores the author name and title
    # Generates a unique string for a given file
"""

    def server_receive_file(self,arg,author_name,paper_title,file_name):
        global count,dictionary,session_list
        m = hashlib.md5()
        lst = []
        count+=1
        with open("files/"+str(paper_title),"wb") as handle:
            handle.write(arg.data)
        uid = m.update(arg.data)
        uid = m.hexdigest()
        if count == 1:
            session_list.append(author_name)
            session_list.append(paper_title)
            session_list.append(file_name)
            dictionary = {uid:session_list}
        else:
            session_list = lst
            dictionary.update({uid:session_list})
        return True

    """
        For a given unique string, it returns the author name
        and the title of a paper
    """

    def paper_send_information(self,uid):
        global dictionary
        return str("Author Name: "+dictionary[uid][0]+"\nTitle: "+dictionary[uid][1])

    """
        Fetches the file from the server and it prints the
        contents
    """

    def print_file_contents(self,uid):
        fd = open(dictionary.values()[0][2],"rb")
        data = fd.readlines()
        return str(data).strip("[]")
    
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost",8000))
server.register_instance(PaperServer())
server.serve_forever()
