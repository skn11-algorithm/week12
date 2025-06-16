import sys
input = sys.stdin.readline

schedule = []
N  = int(input())
for i in range(N):
    schedule.append(list(map(int, input().split())))

print(schedule)


schedule = sorted(schedule, key = lambda x: x[1])

print(schedule)

endtime = 0
count = 0

for i in schedule:
    if i[0] >= endtime:
        endtime = i[1]
        count += 1

print(count)