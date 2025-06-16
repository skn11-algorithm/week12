import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())      
r, c, d = map(int, input().split())       
room = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

# 방향: 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1] 
cleaned_count = 0  

def bfs(x, y, direction):
    global cleaned_count
    queue = deque()
    queue.append((x, y, direction))
    visited[x][y] = 1
    cleaned_count += 1

    while queue:
        x, y, d = queue.popleft()
        found_cleanable = False

        # 4방향을 반시계로 확인
        for _ in range(4):
            d = (d + 3) % 4  # 반시계 방향 회전
            nx, ny = x + dx[d], y + dy[d]

            # 이동 가능한 청소 안된 칸이라면
            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cleaned_count += 1
                queue.append((nx, ny, d))
                found_cleanable = True
                break  # 방향 바꿔 한 칸 이동했으므로 반복 종료

        if not found_cleanable:
            # 후진 좌표 (방향은 유지, 뒤로 한 칸)
            back_x = x - dx[d]
            back_y = y - dy[d]

            if 0 <= back_x < n and 0 <= back_y < m and room[back_x][back_y] == 0:
                queue.append((back_x, back_y, d))  # 후진
            else:
                # 뒤가 벽이면 작동 종료
                break

bfs(r, c, d)
print(cleaned_count)