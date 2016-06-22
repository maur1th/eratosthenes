import sys

n = int(input("Give me an int: "))

if n < 2:
    print("Smallest prime is 2.")
    sys.exit(0)

# Get list of numbers under n
t = list(range(2, n))

i = 0
# Stop once the list has been fully processed
while i < len(t):
    # t[:i + 1], t[i:] overlap at t[i] to avoid keep t[i] in t
    # since t[i] % t[i] == 0
    t = t[:i + 1] + [x for x in t[i:] if x % t[i] != 0]
    # alternative implementation with filter:
    # t = list(filter(lambda x: x % t[i] != 0 or x == t[i], t))
    i += 1

print("Prime numbers under {}: {}".format(n, t))
print("Sum of the primes: {}".format(sum(t)))
