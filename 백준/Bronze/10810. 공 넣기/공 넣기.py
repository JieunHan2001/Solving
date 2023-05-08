n, m = map(int, input().split())
A = [0]*n
for i in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        A[l] = k

print(' '.join(map(str, A)))