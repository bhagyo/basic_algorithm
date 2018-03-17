a = int(input())
key = True

st = (int)(a**(1.0 / 2.0))
if a == 1:
    key = False
for x in range(2, st + 1):
    if(a % x == 0):
        key = False
if key:
    print("prime")
else:
    print("Non prime")
