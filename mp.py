# Multiprocessing

from multiprocessing import Process, Lock

def f(i):
    print "hello world", i
    print "hello duniya", i

for num in range(100):
    Process(target=f, args=(num,)).start()