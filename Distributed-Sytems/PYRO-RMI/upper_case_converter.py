import Pyro4

class ModifyString(object):
    def UPPER(self, name):
        return name.upper()

converter=ModifyString()

daemon=Pyro4.Daemon()                
uri=daemon.register(converter)   

print "Ready. Object uri =", uri      
daemon.requestLoop()                  
