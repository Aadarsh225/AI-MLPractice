'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import math
import sys
import time


## Increase the maximum number of digit for integer conversion
sys.set_int_max_str_digits(100000)


## function to compute factorial

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorail of {number} is {result}")
    return result


if __name__=="__main__":
    numbers=[5000,6000,7000,8000]

    start_time=time.time()
    ## create pool of worker process

    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)

    end_time=time.time()

    print(f"Result:{results}")
    time_taken= end_time - start_time
    print(f"Time taken :{time_taken}")

