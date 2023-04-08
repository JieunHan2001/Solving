A, B = map(int, input().split())
C = int(input())

t_m = (A * 60) + B + C
h = t_m // 60 % 24
m = t_m % 60

print(h, m)