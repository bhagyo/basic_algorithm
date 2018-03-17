import sys


def printf(format, *args):
    sys.stdout.write(format % args)


print("enter the three values as ax^2+bx+c=0")
print("now a,b,c sequentially")
a = int(input())
b = int(input())
c = int(input())
if a == 0:
    print("Invalid")

d = b * b - 4 * a * c
sqrt_val = abs(d)**(1.0 / 2.0)

if d > 0:
    print("Roots are real and different\n")
    print((-b + sqrt_val) / 2 * a)
    print((-b - sqrt_val) / 2 * a)
if d == 0:
    print("Roots are real and same\n")
    print(-b / (2 * a))
else:
    printf("%r - i%r\n", b / (2 * a), sqrt_val)
    printf("%r + i%r\n", b / (2 * a), sqrt_val)
