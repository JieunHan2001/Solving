X = int(input())
N = int(input())
total = 0
for i in range(N):
    a, b = map(int, input().split())
    total = a * b + total
    i += 1
if total == X:
    print("Yes")
else:
    print("No")