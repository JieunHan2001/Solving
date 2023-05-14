m = []
k = []

for i in range(1,31):
    m.append(i)

for i in range(1, 29):
    n = int(input())
    k.append(n)

M = set(m)
K = set(k)
L = M - K

print(min(L))
print(max(list(L))) 