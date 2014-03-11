import SimpleXMLRPCServer

class Repetition:

    def repeat(self, astr, times):
        return astr * times
    
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(Repetition())
server.serve_forever()
