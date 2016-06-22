def fibs(n):
    """
    Yield numbers in the Fibonacci sequence up to its n-th number
    """
    a, b, i = 0, 1, 0
    while i <= n:
        yield a
        a, b, i = b, a + b, i + 1

n = int(input("Give me an int: "))
gen = fibs(n)

result = None
for result in gen:
    pass

print("{}th Fibonacci number is {}".format(n, result))
