'''
연산자 끼워넣기 : 주어진 수에서 연산자를 끼워넣어 나올 수 있는 최댓값, 최솟값
입 : 수의 개수n 수
출 : 결과의 최대 최솟값
'''

# 입력 처리
n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

def calculate_max_min(n, numbers, operators):
    max_val = -1e9
    min_val = 1e9

    def dfs(index, result, plus, minus, multiply, divide):
        nonlocal max_val, min_val

        '''
        종료 조건: 모든 숫자를 한 번씩 사용했으면 (연산자를 다 사용했으면) 최대/최소값 갱신
        '''
        if index == n:
            max_val = max(max_val, result)
            min_val = min(min_val, result)
            return

        next_num = numbers[index]

        '''
        각 연산자가 남아있으면 해당 연산을 수행하고 다음 단계로 재귀 호출
        매 호출마다 연산자 수를 1 줄여서 전달
        '''
        if plus:
            dfs(index + 1, result + next_num, plus - 1, minus, multiply, divide)
        if minus:
            dfs(index + 1, result - next_num, plus, minus - 1, multiply, divide)
        if multiply:
            dfs(index + 1, result * next_num, plus, minus, multiply - 1, divide)
        if divide:
            if result < 0:
                dfs(index + 1, -(-result // next_num), plus, minus, multiply, divide - 1)
            else:
                dfs(index + 1, result // next_num, plus, minus, multiply, divide - 1)


    # 첫 번째 숫자는 그대로 시작하고, 두 번째 숫자부터 연산자를 붙여가며 계산
    dfs(1, numbers[0], *operators)
    return int(max_val), int(min_val)

maximum, minimum = calculate_max_min(n, numbers, operators)
print(maximum)
print(minimum)
