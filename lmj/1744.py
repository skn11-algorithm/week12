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
plus = [] # 양수
minus = [] # 음수
one = 0 # 1 개수 초기화
zero = 0  # 0 개수 초기화
result = 0 # 합산 결과 초기화

for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num == 1:
        one+=1
    elif num == 0:
        zero +=1
    else:
        minus.append(num)

plus.sort(reverse=True) # 큰 수끼리 묶어야되니까 reverse
minus.sort()

'''
양수 음수 소팅하기
[8 6 4 3 2]
[-5 -3 -2 -1]
'''

# 두개씩 묶어서 양수 음수 로직 처리
# for i in range(0, len(plus)-1, 2): 
#     if len(plus) % 2 == 0:
#         result += plus[i] * plus[i+1]
#     else: # 길이가 홀수일때는 나머지 더하는 처리
#         result += plus[i]

# 양수 묶기
for i in range(0, len(plus) - 1, 2):
    result += plus[i] * plus[i+1]
if len(plus) % 2 == 1: # 만약 양수가 하나 남은 상황에서는 plus[-1]는 그냥 더해줌
    result += plus[-1] 

# 음수 묶기
for i in range(0, len(minus)-1, 2):
    result += minus[i] * minus[i+1]
if len(minus) % 2 == 1 and zero == 0: # 만약 음수가 하나 남았고 0의 개수가 없다면 
    result += minus[-1] # 어쩔 수 없이 배열에서 음수 더해주기

# 1처리 : 1은 모두 더해주는 것이 유리함
result += one

print(result)