def solve():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    
    # 방의 상태 입력
    room = []
    for _ in range(n):
        room.append(list(map(int, input().split())))
    
    # 방향: 북(0), 동(1), 남(2), 서(3)
    # 각 방향에 대한 이동 벡터
    dr = [-1, 0, 1, 0]  # 북, 동, 남, 서
    dc = [0, 1, 0, -1]
    
    # 청소한 칸의 개수
    cleaned = 0
    
    # 청소 상태를 표시할 배열 (0: 청소 안됨, 1: 벽, 2: 청소됨)
    cleaned_map = [row[:] for row in room]
    
    while True:
        # 1. 현재 칸이 청소되지 않은 경우 청소
        if cleaned_map[r][c] == 0:
            cleaned_map[r][c] = 2
            cleaned += 1
        
        # 2. 주변 4칸 중 청소되지 않은 빈 칸이 있는지 확인
        has_uncleaned = False
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and cleaned_map[nr][nc] == 0:
                has_uncleaned = True
                break
        
        if not has_uncleaned:
            # 3. 주변에 청소할 곳이 없는 경우 - 후진 시도
            # 현재 방향의 반대 방향으로 후진
            back_direction = (d + 2) % 4
            back_r = r + dr[back_direction]
            back_c = c + dc[back_direction]
            
            # 후진할 수 있는지 확인 (벽이 아닌지)
            if 0 <= back_r < n and 0 <= back_c < m and room[back_r][back_c] != 1:
                r, c = back_r, back_c
            else:
                # 후진할 수 없으면 작동 멈춤
                break
        else:
            # 4. 주변에 청소할 곳이 있는 경우
            # 반시계 방향으로 90도 회전하면서 청소할 곳 찾기
            found = False
            for _ in range(4):
                # 반시계 방향으로 90도 회전
                d = (d - 1) % 4
                
                # 회전한 방향으로 전진할 위치 계산
                nr = r + dr[d]
                nc = c + dc[d]
                
                # 전진할 수 있고 청소되지 않은 빈 칸인 경우
                if 0 <= nr < n and 0 <= nc < m and cleaned_map[nr][nc] == 0:
                    r, c = nr, nc
                    found = True
                    break
            
            # 이론적으로는 has_uncleaned가 True면 반드시 찾을 수 있어야 함
            if not found:
                break
    
    return cleaned

# 결과 출력
print(solve())

# 시간 복잡도: O(NxM) - 최악의 경우 모든 칸을 방문