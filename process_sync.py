import multiprocessing
import sys
import threading
import time

lock = multiprocessing.Lock()

def f(i):
    #with lock:
        for _ in range(10):
            sys.stderr.write(i)
            time.sleep(1)

t1 = threading.Thread(target=f, args=['1'])
t2 = threading.Thread(target=f, args=['2'])
t1.start()
t2.start()
t1.join()
t2.join()