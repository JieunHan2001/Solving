N = int(input())
a = []
a.append(list(map(int, input().split())))

a = [element for sublist in a for element in sublist]
a = sorted(a)
M = max(a)

for i in range(N):
    a[i] = a[i]/M*100
ave = sum(a) / len(a)

print(ave)