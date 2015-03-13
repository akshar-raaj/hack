from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--name", dest="name", help="Input your name")
parser.add_option("-d", "--digit", dest="dig", help="Input digit", default=5)
(options, args) = parser.parse_args()
options.dig = int(options.dig)
print options

def say_hello(name):
    print "Hello %s" % (name,)
    print options.dig + 1

say_hello(options.name)
