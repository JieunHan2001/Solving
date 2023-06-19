T = int(input())

for _ in range(T):
    R, S = input().split()
    P = ''

    for ch in S:
        P += ch * int(R)

    print(P)
