# key M / lock N
# lock을 3N * 3N으로 만들어 정가운데 위치시킨다. (board)
# 각 반복문마다 기존의 board를 deepcopy해 이용 -> 시간 초과로 인해 폐기
# 키 회전 (for) 마다 키를 이동시키면서 돌기에 대해 +1을 해준다.
# board에 키를 더했을 때 자물쇠가 전부 1이라면 true
# 1이 아니라면 키를 다시 빼기(-1 해주기)

def rotate_key(key, m):
    new_key = [[0]*m for _ in range(m)]
    for a in range(m):
        for b in range(m):
            new_key[b][-(a + 1)] = key[a][b]
    return new_key

def solution(key, lock):
    m, n = len(key), len(lock)
    board = [[0]*(3*n) for _ in range(3*n)]
    for a in range(n, 2*n):
        for b in range(n, 2*n):
            board[a][b] = lock[a-n][b-n]
    
    for _ in range(4):
        key = rotate_key(key, m)

        # 키를 옮겨가며 확인
        for a in range(1,2*n):
            for b in range(1, 2*n):
                # 키 꽂기
                for x in range(m):
                    for y in range(m):
                        board[a + x][b + y] += key[x][y]
                # 자물쇠가 열렸는지 확인
                is_open = True
                for x in range(n, 2*n):
                    for y in range(n, 2*n):
                        if board[x][y] != 1:
                            is_open = False             
                # 자물쇠가 열렸으면 True / 안열렸으면 키 빼기
                if is_open:
                    return True
                else:
                    for x in range(m):
                        for y in range(m):
                            board[a + x][b + y] -= key[x][y]
                    
    return False