import sys

input=sys.stdin.readline
n=int(input())

nums=list(map(int,input().rstrip().split()))
# 덧셈, 뺄센, 곱셈, 나눗셈 개수
plus,minus,multi,div=map(int,input().rstrip().split())

max_num=-sys.maxsize
min_num=sys.maxsize

def backtrack(idx,current,plus,minus,multi,div):
    global max_num,min_num
    
    if idx==n:
        max_num=max(max_num,current)
        min_num=min(min_num,current)
        return

    # 0이 아니면
    if plus:
        backtrack(idx+1,current+nums[idx],plus-1,minus,multi,div)
    if minus:
        backtrack(idx+1,current-nums[idx],plus,minus-1,multi,div)
    if multi:
        backtrack(idx+1,current*nums[idx],plus,minus,multi-1,div)      
    if div:
        if current<0:
            backtrack(idx+1,-((-current)//nums[idx]),plus,minus,multi,div-1)      
        else:
            backtrack(idx+1,((current)//nums[idx]),plus,minus,multi,div-1) 

backtrack(1,nums[0],plus,minus,multi,div)
print(max_num)
print(min_num)           
                