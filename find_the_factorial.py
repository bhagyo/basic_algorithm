import sys


def printf(format, *args):
    sys.stdout.write(format % args)


# for printf function as C
a = int(input())
store = 1
for x in range(2, a + 1):
    store *= x

print(store)
