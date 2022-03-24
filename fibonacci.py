#! python3
# Recursive Fibonacci sequence function definition
# For a thorough explanation, visit: https://en.wikipedia.org/wiki/Fibonacci_number

results = dict()

def fibonacci(num):
    global results
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    try:
        return results[num]
    except:
        results[num] = fibonacci(num-1) + fibonacci(num-2)
        return results[num]



print(fibonacci(100))
