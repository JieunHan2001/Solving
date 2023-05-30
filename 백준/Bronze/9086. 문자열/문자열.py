n = int(input())
b = []
for _ in range(n):
    a = input()
    m = len(a)
    b.append(a[0])
    b.append(a[m-1])
i = 0
while i < len(b):
    print(b[i], end = "")
    i += 1
    if i % 2 == 0:
        print()

