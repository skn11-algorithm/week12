import sys
input=sys.stdin.readline
N,M=(map(int,input().rstrip().split())) # 세로(행), 가로(열)

# https://kill-xxx.tistory.com/19
# N=1일때 위아래 못움직이므로 방문 가능한 칸은 1칸

# N=2일때 위아래 1칸씩 움직일 수 있는데
# 4번이상 이동가능할때 4가지 움직임해야하므로
# 가로길이가 어떻든 최대 3번 움직이기 가능, 방문칸은 4칸
# (M+1)//2

# N=3이상일일 때 위 아래 이동 제약 X
# m이 6 이하일 때 min(m, 4)
# m이 7 이상일 때  m - 2

if N==1:
    print(1)
elif N==2:
    if M<=6:
        print((M+1)//2)
    else:
        print(4)
elif N>=3:
    if M<=6:
        print(min(M,4))
    else:
        print(M-2)

