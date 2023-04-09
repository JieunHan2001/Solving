A, B, C = map(int, input().split())
list_1 = [A, B, C]
list_1.sort()
if list_1[0] == list_1[1] == list_1[2]:
    print(10000+(list_1[0]*1000))
elif list_1[0] != list_1[1] != list_1[2]:
    print(list_1[2]*100)
else:
    print(1000+(list_1[1]*100))