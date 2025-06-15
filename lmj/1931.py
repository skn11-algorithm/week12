'''
회의실 배정
입 : 회의 수 N, 회의정보(시작시간 끝나는 시간)
출 : 최대 사용가능한 회의 최대개수
'''
'''
가장 많이이용하려면?
회의 기간이 짧으면서도 종료하자마자 빨리 시작하는 회의 선택하기
'''
import sys
input = sys.stdin.readline

n = int(input())
room = []

for i in range(n):
    start, end = map(int, input().split())
    room.append([start, end])

# 같은 종료시간이면 더 빨리 회의를 선택하기 위해 정렬
# 종료 시간을 오름차순으로 정렬하고, 시간이 같을 댸는 시작 시간 기준으로 정렬)
room.sort(key=lambda x : (x[1], x[0]))

'''
회의 시작 가능한 회의끼리 비교 가능하게 됨
'''

count = 0
end_time = 0 # 마지막으로 선택된 종료 시간을 저장할 변수

for start, end in room:
    if start >= end_time:
        count += 1
        end_time = end

print(count)