A, B = input().split()
A = ''.join(reversed(A))
B = ''.join(reversed(B))

if int(A) > int(B):
    print(A)
else:
    print(B)
