## (1,4) 명령 수행
# (0,10,0,8) 을 4로 자르면
# (0,5,0,8), (5,10,0,8) 이 생긴다

# 해당 숫자가 그 가로/세로 범위 안에 있으면 두 개로 잘린다.
from collections import deque
n, m = map(int, input().split())
squares = [(0, n, 0, m)]

chop = int(input())
for _ in range(chop):
    a, b = map(int, input().split())
    q = deque(squares)
    new_squares = []
    while q:
        x1, x2, y1, y2 = q.popleft()
        # 가로로 자르는 경우
        if a == 0:
            if y1 < b < y2:
                new_squares.append((x1, x2, y1, b))
                new_squares.append((x1, x2, b, y2))
            else:
                new_squares.append((x1, x2, y1, y2))
        # 세로로 자르는 경우
        else:
            if x1 < b < x2:
                new_squares.append((x1, b, y1, y2))
                new_squares.append((b, x2, y1, y2))
            else:
                new_squares.append((x1, x2, y1, y2))
    squares = new_squares
    
max_dimension = 0
for x1, x2 ,y1, y2 in squares:
    max_dimension = max(max_dimension, (x2 - x1) * (y2- y1))

print(max_dimension)