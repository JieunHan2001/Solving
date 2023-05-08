n, m = map(int, input().split())
A = []
for k in range(1, n+1):
    A.append(k)
for l in range(m):
    i, j = map(int, input().split())
    A[i-1], A[j-1] = A[j-1], A[i-1]

print(' '.join(map(str, A)))