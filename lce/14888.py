n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))  # +, -, *, //

max_result = -int(1e9)
min_result = int(1e9)

def dfs(index, result, add, sub, mul, div):
    global max_result, min_result
    if index == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if add:
        dfs(index + 1, result + nums[index], add - 1, sub, mul, div)
    if sub:
        dfs(index + 1, result - nums[index], add, sub - 1, mul, div)
    if mul:
        dfs(index + 1, result * nums[index], add, sub, mul - 1, div)
    if div:
        if result < 0:
            dfs(index + 1, -(-result // nums[index]), add, sub, mul, div - 1)
        else:
            dfs(index + 1, result // nums[index], add, sub, mul, div - 1)

dfs(1, nums[0], operators[0], operators[1], operators[2], operators[3])
print(max_result)
print(min_result)