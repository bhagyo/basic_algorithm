arr = [None] * 1001

arr[0] = 0
arr[1] = 1

for i in range(2, 1000):
    arr[i] = arr[i - 1] + arr[i - 2]

a = int(input())

print(arr[a])
