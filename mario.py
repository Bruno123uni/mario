from cs50 import get_int

while True:
    n = get_int("Positive integer: ")
    if n > 0 and n < 9:
        break


q = n+1
l = 1
w = -1
for g in range(n):

    for x in range(n - l):
        print(" ", end="")
    for w in range(l):
        print("#", end="")
    print()
    l += 1

