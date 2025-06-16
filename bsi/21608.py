def solve():
    n = int(input())
    
    # 학생별 좋아하는 학생들 저장
    preferences = {}
    order = []
    
    for _ in range(n * n):
        line = list(map(int, input().split()))
        student = line[0]
        likes = set(line[1:5])
        preferences[student] = likes
        order.append(student)
    
    # 교실 초기화 (0은 빈 자리)
    classroom = [[0] * n for _ in range(n)]
    
    # 방향벡터 (상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def get_adjacent_cells(x, y):
        """(x, y) 위치의 인접한 셀들을 반환"""
        adjacent = []
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                adjacent.append((nx, ny))
        return adjacent
    
    def find_best_position(student):
        """학생을 배치할 최적의 위치를 찾는 함수"""
        best_positions = []
        max_liked_count = -1
        max_empty_count = -1
        
        for i in range(n):
            for j in range(n):
                if classroom[i][j] != 0:  # 이미 학생이 있는 자리
                    continue
                
                adjacent = get_adjacent_cells(i, j)
                liked_count = 0  # 인접한 좋아하는 학생 수
                empty_count = 0  # 인접한 빈 자리 수
                
                for ax, ay in adjacent:
                    if classroom[ax][ay] == 0:
                        empty_count += 1
                    elif classroom[ax][ay] in preferences[student]:
                        liked_count += 1
                
                # 우선순위에 따라 최적 위치 결정
                if (liked_count > max_liked_count or 
                    (liked_count == max_liked_count and empty_count > max_empty_count)):
                    max_liked_count = liked_count
                    max_empty_count = empty_count
                    best_positions = [(i, j)]
                elif (liked_count == max_liked_count and empty_count == max_empty_count):
                    best_positions.append((i, j))
        
        # 행, 열 번호가 가장 작은 위치 선택
        best_positions.sort()
        return best_positions[0]
    
    # 학생들을 순서대로 배치
    for student in order:
        x, y = find_best_position(student)
        classroom[x][y] = student
    
    # 만족도 계산
    satisfaction_scores = [0, 1, 10, 100, 1000]
    total_satisfaction = 0
    
    for i in range(n):
        for j in range(n):
            student = classroom[i][j]
            adjacent = get_adjacent_cells(i, j)
            liked_adjacent_count = 0
            
            for ax, ay in adjacent:
                if classroom[ax][ay] in preferences[student]:
                    liked_adjacent_count += 1
            
            total_satisfaction += satisfaction_scores[liked_adjacent_count]
    
    return total_satisfaction

# 결과 출력
print(solve())