'''
상어초
'''
import sys

input = sys.stdin.readline

N = int(input())
students_info = [list(map(int, input().split())) for _ in range(N * N)]

grid = [[0] * N for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 학생별 좋아하는 친구 정보 저장
likes = {student[0]: set(student[1:]) for student in students_info}

def get_candidate_positions(student):
    candidates = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                continue

            like_cnt = 0
            empty_cnt = 0

            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < N and 0 <= nj < N:
                    if grid[ni][nj] == 0:
                        empty_cnt += 1
                    elif grid[ni][nj] in likes[student]:
                        like_cnt += 1

            candidates.append((like_cnt, empty_cnt, i, j))
    '''
    우선순위: 좋아하는 학생 수 ↓, 비어있는 인접 자리 수 ↓, 행 ↑, 열 ↑
    => 좋아하는 수 내림차순, 빈칸 수 내림차순, 행 오름차순, 열 오름차순
    '''
    candidates.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    return candidates

# 자리 배치
for student in students_info:
    student_id = student[0]
    best = get_candidate_positions(student_id)[0]
    x, y = best[2], best[3]
    grid[x][y] = student_id

def calculate_satisfaction():
    total = 0
    for i in range(N):
        for j in range(N):
            student = grid[i][j]
            like_count = 0
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] in likes[student]:
                    like_count += 1
            if like_count > 0:
                total += 10 ** (like_count - 1)
    return total

print(calculate_satisfaction())