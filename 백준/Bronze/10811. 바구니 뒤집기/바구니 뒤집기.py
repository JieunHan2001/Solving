N,M = map(int, input().split())
a = []

for k in range(1, N+1):
    a.append(k)

for _ in range(M):
    i, j = map(int, input().split())
    reversed_slice = a[i - 1:j][::-1]
    a[i - 1 :j] = reversed_slice

print(' '.join(map(str, a)))

