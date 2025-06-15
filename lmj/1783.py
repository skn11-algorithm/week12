'''
병든 나이트 : 병든 나이트는 2위 1오 / 1위 2오 / 1칸 아래 2칸오 / 2칸 아래 1칸오

입 : 체스판 세로 N 가로 M
출 : 나이트가 방문할 수 있는 최댓값
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
'''
💡예제해보기
세로 1 가로 1이면
ㅁ 
현재위치 1칸만 방문 가능

세로 2 가로 4이면
ㅁㅁㅁㅁ
ㅁㅁㅁㅁ
1위2오, 1아2오 로
처음위치, 도달위치 2칸 방문 가능
'''

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m-1)//2+1))
elif m <= 6:
    print(min(4, m))
else:
    print(m-2)