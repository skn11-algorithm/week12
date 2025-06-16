import sys
input = sys.stdin.readline

N = int(input())
pos = []
neg = []
ones = 0
zeros = 0
result = 0

for _ in range(N):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num == 1:
        ones += 1  # 1은 그냥 더하는 게 이득
    elif num == 0:
        zeros += 1
    else:
        neg.append(num)

# 양수는 큰 수끼리 곱해야 이득
pos.sort(reverse=True)
# 음수는 작은 수끼리 곱해야 이득
neg.sort()

# 양수 처리
for i in range(0, len(pos)-1, 2):
    result += pos[i] * pos[i+1]
if len(pos) % 2 == 1:
    result += pos[-1]

# 음수 처리
for i in range(0, len(neg)-1, 2):
    result += neg[i] * neg[i+1]
if len(neg) % 2 == 1:
    if zeros > 0:
        pass  # 0과 곱해서 없애는 것이 이득
    else:
        result += neg[-1]

# 1은 그냥 더하기
result += ones

print(result)