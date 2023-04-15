list_A = []
for i in range(9):
    a = int(input())
    list_A.append(a)
    i += 1
print(max(list_A), int(list_A.index(max(list_A))+1))