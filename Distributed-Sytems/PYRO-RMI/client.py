import Pyro4

uri=raw_input("Enter your URI : ").strip()
string=raw_input("Enter any string? ").strip()

converter=Pyro4.Proxy(uri)          # get a Pyro proxy to the greeting object
print converter.UPPER(string)   # call method normally
