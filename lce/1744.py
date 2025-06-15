n = int(input())
pos, neg = [], []
zero = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num == 1:
        zero += 1
    elif num == 0:
        zero += 1
    else:
        neg.append(num)

pos.sort(reverse=True)
neg.sort()

def pair_sum(arr):
    result = 0
    for i in range(0, len(arr)-1, 2):
        result += arr[i] * arr[i+1]
    if len(arr) % 2 == 1:
        result += arr[-1]
    return result

answer = pair_sum(pos) + pair_sum(neg)
print(answer)
