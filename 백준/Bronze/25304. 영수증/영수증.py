ans = int(input())
n = int(input())

total = 0
for _ in range(n):
    price, num = map(int, input().split())
    total += price*num
if ans == total:
    print("Yes")
else:
    print("No")