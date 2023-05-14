a = []
for i in range(10):
    n = int(input())
    m = n % 42
    a.append(m)

b = set(a)
a = list(b)

print(len(a))
