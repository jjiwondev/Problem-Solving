ans = int(input())
n = int(input())

total = 0
for _ in range(n):
    price, num = map(int, input().split())
    total += price*num

print("Yes") if ans == total else print("No")
