list = [1, 4]
for i in range(20):
    list.append(list[i-1]+list[i-2])
print(list)
