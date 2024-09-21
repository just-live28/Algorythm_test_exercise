# n * m 카드 (행, 렬)
# 행 선택 / 가장 낮은 카드 뽑기 / 

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = []
for row in board:
    result.append(min(row))

print(max(result))