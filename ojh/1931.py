import sys

input=sys.stdin.readline

N=int(input())
time=[]
for _ in range(N):
    s,e=(map(int,input().rstrip().split()))
    time.append((s,e))

# 빨리 끝나는 회의 선택하면 남은 시간대가 최대화

# 회의의 시작시간과 끝나는 시간이 같을 수도 있으므로
# 시작시간도 오름차순 정렬해야 함

# ex )
# (2 2) (1 2) 가 있을때 (1 2)->(2 2) 회의 2번해야함
time.sort(key=lambda x:(x[1],x[0]))

count=0
current_end=0

for s,e in time:
    if s>=current_end:
        count+=1
        current_end=e

print(count)