import sys
n = int(input())
s = ""
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)