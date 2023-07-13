c_list = []
for _ in range(10):
    a = int(input())%42
    if a not in c_list:
        c_list.append(a)
print(len(c_list))
