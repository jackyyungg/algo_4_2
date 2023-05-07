import time
import matplotlib.pyplot as plt

def F_dynamic(n):
    fib = [0] * (n+1)
    fib[1] = 1
    fib[2] = 1
    for i in range(3, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

def measure_execution_time(function, n):
    start_time = time.time()
    k = function(n)
    end_time = time.time()
    return end_time - start_time, k

n_values = list(range(10, 101, 10))
recursive_times = []
dynamic_times = []

for n in n_values:
    dynamic_time, k_dynamic = measure_execution_time(F_dynamic, n)
    print('n:',n, end =' ')
    print('result:',k_dynamic, end =' ')
    print('dynamic time:',dynamic_time)

 #when the maximum value of n such that computing F(n+1) recursively causes computer to crash
n = 50
dynamic_time, k_dynamic = measure_execution_time(F_dynamic, n+1)
print('n:',n+1, end =' ')
print('result:', k_dynamic, end =' ')
print('dynamic time:', dynamic_time)
