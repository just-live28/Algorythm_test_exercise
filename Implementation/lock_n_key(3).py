# 키를 움직여 가면서 / 돌려 가면서 자물쇠에 맞춰보기
# 자물쇠의 모든 칸이 1이 되어야 함. (돌기 돌기가 만나면 2) (홈이 안채워지면 0)
# 키를 넣어보고 맞춰지면 return True / 안맞춰지면 다시 뺀 후 다음 케이스로 넘기기

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

def rotate_key(key):
    l = len(key)
    
    nkey = [[0]*l for _ in range(l)]
    
    for a in range(l):
        for b in range(l):
            nkey[a][b] = key[b][-(a+1)]
    
    return nkey

def solution(key, lock):
    length = len(lock)
    board = [[0] * (3*length) for _ in range(3*length)]

    for a in range(length, 2*length):
        for b in range(length, 2*length):
            board[a][b] = lock[a-length][b-length]

    for _ in range(4):
        key = rotate_key(key)
        for a in range(length-len(key) + 1, 2*length):
            for b in range(length-len(key) + 1, 2*length):
                #key 삽입
                for x in range(len(key)):
                    for y in range(len(key)):
                        board[a+x][b+y] += key[x][y]
                #lock 확인
                enable = True
                for x in range(length, 2*length):
                    for y in range(length, 2*length):
                        if board[x][y] != 1:
                            enable = False
                #lock이 열렸으면 true 반환
                if enable:
                    return True
                #key 해제
                for x in range(len(key)):
                    for y in range(len(key)):
                        board[a+x][b+y] -= key[x][y]

    return False

print(solution(key, lock))