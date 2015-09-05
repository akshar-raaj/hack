import cProfile, pstats, StringIO
import time

def one():
    print "hello"
    for i in range(1000):
        pass
    two()

def two():
    time.sleep(1)

pr = cProfile.Profile()
pr.enable()
one()
pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()