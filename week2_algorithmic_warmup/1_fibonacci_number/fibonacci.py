# Uses python3

import time
startTime = time.time()

# Naive Solution
# def calc_fib(n):
#     if (n <= 1):
#         return n

#     return calc_fib(n - 1) + calc_fib(n - 2)

# Efficient solution

fibArray = [0, 1]
def calc_fib(n):

    if n <= 1:
        return n

    for i in range(n):
        fibArray[i-1], fibArray[i] = fibArray[i], fibArray[i-1] + fibArray[i] 
        fibArray.append(fibArray[i])

    return fibArray[-1]

n = int(input())
print(calc_fib(n))

print("--- This piece of code runs in ---" % (time.time() - startTime))
