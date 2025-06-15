import sys

sys.setrecursionlimit(150000)

input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
r,c,d=map(int,input().rstrip().split())

# 북동남서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 반시계 방향 90도 회전
# 북(0) -> 서(3)
# 동(1) -> 북(0)
# 남(2) -> 동(1)
# 서(3) -> 남(2)
# (원래+3)%4

# 후진
# 북(0) -> 남(2)
# 동(1) -> 서(3)
# 남(2) -> 북(0)
# 서(3) -> 동(1)
# (원래+2)%4

def dfs(x,y,d):
    global count
    if arr[x][y]==0:
        count+=1
        arr[x][y]=2
    for _ in range(4):
        nd=(d+3)%4
        nx,ny=x+dx[nd],y+dy[nd]
        if 0<=nx<N and 0<=ny<M and arr[nx][ny]==0:
            dfs(nx,ny,nd)
            return
        d=nd

    nd=(d+2)%4
    nx,ny=x+dx[nd],y+dy[nd]
    if 0<=nx<N and 0<=ny<M and arr[nx][ny]!=1:
        dfs(nx,ny,d)


arr=[list(map(int,input().rstrip().split())) for _ in range(N)]
count=0
dfs(r,c,d)
print(count)