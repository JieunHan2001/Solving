N = int(input())
M = 2 * N - 1

for k in range(1, M + 1):
    if (k % 2) == 1:
        spaces = " " * ((M - k) // 2)
        stars = "*" * k
        print(spaces + stars, sep="")

for k in range(M - 2, 0, -2):
    spaces = " " * ((M - k) // 2)
    stars = "*" * k
    print(spaces + stars, sep="")
