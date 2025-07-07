# Print out the first n items of the Fibonacci series
def print_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

print_fibonacci(5)