import sys

input=sys.stdin.readline
n = int(input().rstrip())
data = [[0]*n for _ in range(n)]
students = [list(map(int, input().rstrip().split())) for _ in range(n**2)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 학생 한명씩 배치
for student in students:
    available = [] # 가능한 좌석 후보

    for i in range(n):
        for j in range(n):
            if data[i][j] == 0: # 빈자리면
                prefer, empty = 0, 0 # 인접한 좋아하는 학생 수, 빈칸 수

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if data[nx][ny] in student[1:]: # 좋아하는 학생이 인접해 있다면
                            prefer += 1
         
                        if data[nx][ny] == 0: # 인접한 자리가 비어 있다면
                            empty += 1
                 # 가능한 자리 후보에 (행, 열, 좋아하는 학생 수, 빈칸 수) 추가
                available.append((i, j, prefer, empty))
    
    # 조건에 맞게 정렬: 좋아하는 학생 수 ↓, 빈 칸 수 ↓, 행 ↑, 열 ↑
    available.sort(key= lambda x: (-x[2], -x[3], x[0], x[1]))
    data[available[0][0]][available[0][1]] = student[0]

answer = 0 # 최종 만족도 점수
score = [0,1,10,100,1000] # 인접한 좋아하는 학생 수에 따른 점수
students.sort() # 학생 번호 순으로 정렬

# 각 자리에 대해 만족도 점수 계산
for i in range(n):
    for j in range(n):
        count = 0 # 인접한 좋아하는 학생 수

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                # 인접한 칸에 좋아하는 학생이 있는 경우
                if data[nx][ny] in students[data[i][j] - 1]:
                    count += 1

        answer += score[count] # 만족도 점수 누적

print(answer)


