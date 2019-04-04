# - What is the problem in the following code?
# - How do you solve it?
# - Will it happen the same problem using processes instead of threads. Why?

# ```
import threading
import time
import random

total = 0
lock = threading.Lock()

def update_total(amount, delay):
    global total
    time.sleep(delay)
    with lock:
        total0 = total
        total = total0 + amount

threads = []
transactions = [2, 100, 20, 300, 400, 250, 15, 89]

for amount in transactions:
    mythread = threading.Thread(target=update_total, args=[amount, random.randint(3, 6)])
    mythread.start()
    threads.append(mythread)

for t in threads:
    t.join()

print(sum(transactions), total)


# What is the problem in the following code ?
# The problem in the code is in this case same threads are
# increasing the total variable at the same time what is not
# thread safe because os is controlling when the thread runs 
# and when it gets swapped out to let another thread run. 
# This thread swapping can occur at any point in the execution,
# it’s possible for this swap to happen after a thread has read 
# the value but before it has had the chance to write it back.
# This cause crashes or other bugs that in this case
# total is not calculated correctly.
#

#How do you Solve it:
# I would solve it using a lock (threading.Lock()) to protect
# shaed mutable state:
# with lock:
#        total0 = total
#        total = total0 + amount

# - Will it happen the same problem using processes instead of threads. Why?
#multiprocessing contains equivalents of all the synchronization primitives 
# from threading. We would need a locker too.