import xmlrpclib,os,sys

def commands():
    print "1. Add Author name and Paper Title"
    print "2. List the Contents in the server"
    print "3. Display the author and title of a paper"
    print "4. View the contents of a paper"

def core():
    input_option = input("Enter your choice:")
    server = xmlrpclib.Server("http://localhost:8000")
    if input_option == 2:
        print server.list()
        status = raw_input("Still do you want to continue? Y or N:")
        if status == "Y" or status == "y":
            commands()
            core()
        else:
            pass
    if input_option == 1:
        author_name = raw_input("Enter the author name:")
        paper_title = raw_input("Enter the Paper Title:")
        with open(sys.argv[1],"rb") as handle:
            binary_data = xmlrpclib.Binary(handle.read())
        server.server_receive_file(binary_data,author_name,paper_title)
        status = raw_input("Still do you want to continue? Y or N:")
        if status == "Y" or status == "y":
            commands()  
            core()
        else:
            pass
commands()
core()
