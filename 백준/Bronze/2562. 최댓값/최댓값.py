max = -1
index = -1
for idx in range(9):
    num = int(input())
    if(num > max):
        index = idx+1
        max = num
print(max)
print(index)
