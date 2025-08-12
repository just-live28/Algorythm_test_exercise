from collections import deque

def solution(board):
    n = len(board)
    nboard = [[1] * (n+2) for _ in range(n+2)]
    for i in range(1, n+1):
        nboard[i] = [1] + board[i-1] + [1]
    
    q = deque()
    # (count, x1, y1, x2, y2)
    q.append((0, 1, 1, 1, 2))
    visited = set()
    # 0 가로 1 세로 / 가로 축은 왼쪽 좌표 / 세로 축은 위쪽 좌표
    # (0/1, 축x좌표, 축y좌표)
    visited.add((0, 1, 1))
    while q:
        count, x1, y1, x2, y2 = q.popleft()
        
        if (x1, y1) == (n, n) or (x2, y2) == (n, n):
            return count
        
        # 가로로 놓인 경우
        if x1 - x2 == 0:
            # 위쪽이 빈 경우
            if nboard[x1-1][y1] == 0 and nboard[x1-1][y2] == 0:
                # 위쪽으로 이동하는 경우
                if (0, x1-1, y1) not in visited:
                    visited.add((0, x1-1, y1))
                    q.append((count+1, x1-1, y1, x1-1, y2))
                # 위쪽으로 좌회전하는 경우
                if (1, x1-1, y1) not in visited:
                    visited.add((1, x1-1, y1))
                    q.append((count+1, x1-1, y1, x1, y1))
                # 위쪽으로 우회전하는 경우
                if (1, x1-1, y2) not in visited:
                    visited.add((1, x1-1, y2))
                    q.append((count+1, x1-1, y2, x2, y2))
            # 아래쪽이 빈 경우
            if nboard[x1+1][y1] == 0 and nboard[x1+1][y2] == 0:
                # 아래쪽으로 이동하는 경우
                if (0, x1+1, y1) not in visited:
                    visited.add((0, x1+1, y1))
                    q.append((count+1, x1+1, y1, x1+1, y2))
                # 아래쪽으로 좌회전하는 경우
                if (1, x1, y1) not in visited:
                    visited.add((1, x1, y1))
                    q.append((count+1, x1, y1, x1+1, y1))
                # 아래쪽으로 우회전하는 경우
                if (1, x2, y2) not in visited:
                    visited.add((1, x2, y2))
                    q.append((count+1, x2, y2, x1+1, y2))
            # 왼쪽으로 이동하는 경우
            if nboard[x1][y1-1] == 0 and (0, x1, y1-1) not in visited:
                visited.add((0, x1, y1-1))
                q.append((count+1, x1, y1-1, x1, y1))
            # 오른쪽으로 이동하는 경우
            if nboard[x1][y2+1] == 0 and (0, x2, y2) not in visited:
                visited.add((0, x2, y2))
                q.append((count+1, x2, y2, x2, y2+1))
        # 세로로 놓인 경우
        elif y1 - y2 == 0:
            # 위쪽으로 이동하는 경우
            if nboard[x1-1][y1] == 0 and (1, x1-1, y1) not in visited:
                visited.add((1, x1-1, y1))
                q.append((count+1, x1-1, y1, x1, y1))
            # 아래쪽으로 이동하는 경우
            if nboard[x2+1][y1] == 0 and (1, x2, y2) not in visited:
                visited.add((1, x2, y2))
                q.append((count+1, x2, y2, x2+1, y2))
            # 왼쪽이 빈 경우
            if nboard[x1][y1-1] == 0 and nboard[x2][y1-1] == 0:
                # 왼쪽으로 이동하는 경우
                if (1, x1, y1-1) not in visited:
                    visited.add((1, x1, y1-1))
                    q.append((count+1, x1, y1-1, x2, y2-1))
                # 왼쪽으로 좌회전하는 경우
                if (0, x2, y1-1) not in visited:
                    visited.add((0, x2, y1-1))
                    q.append((count+1, x2, y1-1, x2, y2))
                # 왼쪽으로 우회전하는 경우
                if (0, x1, y1-1) not in visited:
                    visited.add((0, x1, y1-1))
                    q.append((count+1, x1, y1-1, x1, y1))
            # 오른쪽이 빈 경우
            if nboard[x1][y1+1] == 0 and nboard[x2][y1+1] == 0:
                # 오른쪽으로 이동하는 경우
                if (1, x1, y1+1) not in visited:
                    visited.add((1, x1, y1+1))
                    q.append((count+1, x1, y1+1, x2, y1+1))
                # 오른쪽으로 좌회전하는 경우
                if (0, x1, y1) not in visited:
                    visited.add((0, x1, y1))
                    q.append((count+1, x1, y1, x1, y1+1))
                # 오른쪽으로 우회전하는 경우
                if (0, x2, y2) not in visited:
                    visited.add((0, x2, y2))
                    q.append((count+1, x2, y2, x2, y1+1))