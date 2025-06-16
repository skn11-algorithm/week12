n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        count += 1

    cleaned = False

    for _ in range(4):
        d = (d + 3) % 4  
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            r, c = nx, ny
            cleaned = True
            break

    if cleaned:
        continue

    back = (d + 2) % 4
    br = r + dx[back]
    bc = c + dy[back]

    if 0 <= br < n and 0 <= bc < m and room[br][bc] != 1:
        r, c = br, bc
    else:
        break  

print(count)
