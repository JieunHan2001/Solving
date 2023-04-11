N = int(input())
list_1 = list(map(int, input().split()))
v = int(input())

count = 0
for i in range(N):
    if list_1[i] == v:
        count += 1

print(count)