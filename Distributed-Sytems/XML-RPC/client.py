import xmlrpclib


server = xmlrpclib.Server('http://localhost:8000')

text = raw_input("Enter the string:")
count = int(raw_input("Enter the no of times to repeat:"))
print server.repeat(text+'\n', count)
