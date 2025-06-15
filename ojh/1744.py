import sys

input=sys.stdin.readline
n=int(input())
nums=[ int(input()) for _ in range(n)]

if n==1:
    print(nums[0])
    exit()

nums.sort()
nums_0=[num for num in nums if num<=0]
nums_1=[num for num in nums if num==1]
nums_2=[num for num in nums if num>=2]

count=0

# 0또는 음수
if len(nums_0)==0:
    pass
elif len(nums_0)==1:
    count+=nums_0[0]
else:
    # 짝수 개수까지 곱하고, 남는 하나는 마지막에 더함(길이가 홀수일 때를 대비)
    for i in range(0,len(nums_0)-1,2):
        count+=(nums_0[i]*nums_0[i+1])
    if len(nums_0)%2!=0:
        count+=nums_0[-1]

# 1일 때
count+=(len(nums_1)*1)

# 2이상일 때
if len(nums_2)==0:
    pass
elif len(nums_2)==1:
    count+=nums_2[0]
else:
    for i in range(len(nums_2)-1,0,-2):
        count+=(nums_2[i]*nums_2[i-1])

    # 개수가 홀수일 때
    if len(nums_2)%2!=0:
        count+=nums_2[0]

print(count)