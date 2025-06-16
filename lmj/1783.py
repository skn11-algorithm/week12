'''
병든 나이트 : 병든 나이트는 2위 1오 / 1위 2오 / 1칸 아래 2칸오 / 2칸 아래 1칸오/ 로만 움직일 수 있음
입 : 체스판 가로 N 세로 M
출 : 나이트가 방문할 수 있는 최댓값
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m-1)//2+1))
elif m <= 6:
    print(min(4, m))
else:
    print(m-2)