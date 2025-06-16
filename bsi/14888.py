import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))  # +, -, *, /

max_result = -int(1e9)
min_result = int(1e9)

def dfs(index, current, add, sub, mul, div):
    global max_result, min_result

    if index == N:
        max_result = max(max_result, current)
        min_result = min(min_result, current)
        return

    num = numbers[index]

    if add:
        dfs(index + 1, current + num, add - 1, sub, mul, div)
    if sub:
        dfs(index + 1, current - num, add, sub - 1, mul, div)
    if mul:
        dfs(index + 1, current * num, add, sub, mul - 1, div)
    if div:
        if current < 0:
            dfs(index + 1, -(-current // num), add, sub, mul, div - 1)
        else:
            dfs(index + 1, current // num, add, sub, mul, div - 1)

dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

print(max_result)
print(min_result)