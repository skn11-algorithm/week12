'''
수 묶기 : 각 수를 두 개씩 묶었을때(곱) 수열 합이 최대가 되도록 하기
입 : 수열 길이 N, 각 수열
출 : 최대 합

절대값 큰 음수 두개 곱하고, 0은 다른 음수랑 곱해 처리, 1은 더하는게 유리하고, 양수는 가장 큰 애끼리 곱하는게 최대
일단 부호별로 리스트에 입력받고 sort해보자 (0과 1은 안묶고 바로 처리해주자)
'''

import sys
input = sys.stdin.readline

n = int(input())
plus = []   # 양수
minus = []  # 음수
one = 0     # 1 개수
zero = 0    # 0 개수
result = 0  # 결과 합계

for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)  # 오타 수정: appned -> append
    elif num == 1:
        one += 1
    elif num == 0:
        zero += 1
    else:
        minus.append(num)

# 큰 양수끼리 곱해야 하므로 내림차순
plus.sort(reverse=True)
# 절댓값 큰 음수끼리 곱해야 하므로 오름차순
minus.sort()

# 양수 묶기
for i in range(0, len(plus) - 1, 2):
    result += plus[i] * plus[i + 1]
if len(plus) % 2 == 1:
    result += plus[-1]  # 남은 1개 그냥 더함

# 음수 묶기
for i in range(0, len(minus) - 1, 2):
    result += minus[i] * minus[i + 1]

# 음수 하나 남았을 때 0으로 처리할 수 없으면 그냥 더함
if len(minus) % 2 == 1 and zero == 0:
    result += minus[-1]
    
# 1은 모두 더하기
result += one

print(result)
