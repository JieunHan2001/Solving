import sys

T = int(sys.stdin.readline())
for x in range(T):
    A, B = map(int, input().split())
    print(f"Case #{x+1}: {A + B}")