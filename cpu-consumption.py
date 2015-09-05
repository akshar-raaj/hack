"""
I want to check how number of threads/processes affect cpu utilization

### Initial expectations
Then I start 4 threads, so this again should execute in same time because I have 4 logical cores.
Then I start 8 threads, so time required to execute this should go up by 2 times.
"""

"""
My machine has 4 logical cores which I understand means that 4 processes/threads
could be running simultaneously, i.e parallely in actual sense, i.e multithreading
and not multitasking

I will start 1 thread which will keep on doing simple mathematical operation for around
a minute, i.e it loops through 10000000 times.
1 thread takes "It took 5.67828798294 seconds."
utilization of 2 cores go up even with single thread.
2 thread takes "It took 16.8707869053 seconds."
2 threads, utilization of 2 CPU go up. Even for 3rd and 4th it seems like they are going up. Is there is something wrong with htop or what I am seeing is specific to Python and will be different for other languages?
With 3 threads, utilization of all CPUS is shown
With 3 threads "It took 47.1474311352 seconds.". Why is it taking more time with threads than with processes? GIL.

Let me try multprocessing
1 process takes "It took 5.81162214279 seconds."
I am using htop and see utilization of two of my cores going up when using a single process. So it seems like a process spreads it's work over multiple cores?
2 process take "It took 6.25350904465 seconds."
Seeing the utilization of 4 cores going up, so seems all the cores are utilized even if 2 processes are running.
3 process take "It took 24.0174770355 seconds."

Changed the multiprocesses program
So that each loop iteration is dependent on last loop iteration
    s = s + 1 + 1
    return s
1 process "It took 8.94253015518 seconds."

Take a machine with 8 cores and see how fast this same program is.
"""

from threading import Thread
from multiprocessing import Process
import time

MAX = 100000000

class SumThread(Thread):

    def run(self):
        for i in range(MAX):
            a = 1 + 1

def sum():
    s = 0
    for i in range(MAX):
        s = s + 1 + 1
    print s

start = time.time()
#threads = []
processes = []
for i in range(3):
    #st = SumThread()
    #threads.append(st)
    #st.start()
    p = Process(target=sum)
    processes.append(p)
    p.start()

#for t in threads:
    #t.join()

for p in processes:
    p.join()

print 'It took', time.time()-start, 'seconds.'