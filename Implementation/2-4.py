def rotate_key(key):
    new_key = [[0] * len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            new_key[j][-(i+1)] = key[i][j]    
    return new_key

def check_lock(board, n):
    for a in range(n, 2 * n):
        for b in range(n, 2 * n):
            if board[a][b] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    board = [[0] * (3 * n) for _ in range(3 * n)]
    
    # 자물쇠 이식
    for i in range(n):
        for j in range(n):
            board[n + i][n + j] = lock[i][j]
    
    for _ in range(4):
        key = rotate_key(key)
        
        # 키 이동
        for i in range(2 * n):
            for j in range(2 * n):
                # 키 삽입
                for a in range(len(key)):
                    for b in range(len(key)):
                        board[i+a][j+b] += key[a][b]
                
                # 자물쇠가 열린지 확인
                if check_lock(board, n):
                    return True
                else:
                    # 열리지 않으면 키 제거
                    for a in range(len(key)):
                        for b in range(len(key)):
                            board[i+a][j+b] -= key[a][b]
    
    return False