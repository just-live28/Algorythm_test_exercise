def rotate_key(key):
    M = len(key[0])
    new_key = [[0] * M for _ in range(M)]
    
    for a in range(M):
        for b in range(M):
            new_key[b][-(a+1)] = key[a][b]

    return new_key

def check_lock(board, N):
    for a in range(N, 2*N):
        for b in range(N, 2*N):
            if board[a][b] != 1:
                return False
    return True

def solution(key, lock):
    N = len(lock[0])
    M = len(key[0])
    
    board = [[0] * (3*N) for _ in range(3*N)]
    for i in range(N, 2*N):
        for j in range(N, 2*N):
            board[i][j] = lock[i-N][j-N]
    
    for _ in range(4):
        key = rotate_key(key)
        
        for i in range(2*N):
            for j in range(2*N):
                # 키 더하기
                for a in range(M):
                    for b in range(M):
                        board[i+a][j+b] += key[a][b]
                
                # 자물쇠가 모두 채워졌는지 확인
                if check_lock(board, N):
                    return True
                
                # 키 빼기
                for a in range(M):
                    for b in range(M):
                        board[i+a][j+b] -= key[a][b]

    return False