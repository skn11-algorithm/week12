n = int(input())
students = [list(map(int, input().split())) for _ in range(n * n)]
seat = [[0] * n for _ in range(n)]

# 학생 순서대로 배치
for student in students:
    num = student[0]
    like = student[1:]

    candidates = []
    for i in range(n):
        for j in range(n):
            if seat[i][j] != 0:
                continue
            like_cnt = 0
            empty_cnt = 0
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n:
                    if seat[ni][nj] in like:
                        like_cnt += 1
                    if seat[ni][nj] == 0:
                        empty_cnt += 1
            candidates.append(( -like_cnt, -empty_cnt, i, j ))

    # 조건 1 → 2 → 3 → 4 순 정렬 (음수로 정렬)
    candidates.sort()
    x, y = candidates[0][2], candidates[0][3]
    seat[x][y] = num

# 만족도 계산
position = {}
for i in range(n):
    for j in range(n):
        position[seat[i][j]] = (i, j)

score = 0
score_map = [0, 1, 10, 100, 1000]

for student in students:
    num, like = student[0], student[1:]
    x, y = position[num]
    cnt = 0
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if seat[nx][ny] in like:
                cnt += 1
    score += score_map[cnt]

print(score)
