### Multi Threading
## When to use Multi THreading
## I/O-bound task :Taska that spends more time waiting fro I/o operation
## Concurrent execution improve the throughput of your application

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Numbers:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")

## create 2 thread 
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)


t = time.time()
### start the thread
t1.start()
t2.start()

### Wait for thread to complete
t1.join()
t2.join()
print_letter()
finished_time = time.time() - t
print(finished_time)
