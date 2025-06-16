n, m = map(int, input().split())
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 본 문제에서는 없어도 통과되지만, 범위 안에서 이동하는지 확인하기 위해 필요함
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def cleaner(x, y, d):
    cnt = 0
    while True:
        # 1번 청소하고 청소 횟수 1 증가
        if area[x][y] == 0:
            area[x][y] = -1 # 청소함
            cnt += 1

        # 3번 반시계 방향으로 회전하며 청소하지 않은 칸 탐색
        for _ in range(4):
            d = (d - 1) % 4
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny) and area[nx][ny] == 0:  # 청소 안한 칸으로 이동
                x, y = nx, ny
                break # 이동했으면 다시 1번으로

        else:
            # 2번 4칸다 깨끗하다면 후진하거나 멈춤
            x, y = x + dx[d] * (-1), y + dy[d] * (-1) # 후진
            if in_range(x, y) and area[x][y] == 1 or not in_range(x,y):  # 벽이라면 작동 멈춤
                print(cnt)
                return

cleaner(r, c, d)