import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [2, 1, -1, -2]
dy = [1, 2, 2, 1]

x = 0
y = 0
total = 0
def greedy(x, y, total):
    count = 1
    nx, ny = x, y

    if N < 3 or M < 7:
        if N == 1:
            count = 1
        elif N == 2:
            count = min(4, (M + 1) // 2)
        else:
            count = min(4, M)
    else:
        count = M - 2

    return count

print(greedy(x, y, total))
