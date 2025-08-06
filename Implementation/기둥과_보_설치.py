def add_frame(cols, rows, frame, result):
    fx, fy, ftype, _ = frame

    result.append([fx, fy, ftype])
    if ftype == 0: # 기둥 설치
        cols[fx][fy] = True
    else:   # 보 설치
        rows[fx][fy] = True

def del_frame(cols, rows, frame, result):
    fx, fy, ftype, _ = frame

    result.remove([fx, fy, ftype])
    if ftype == 0:  # 기둥 삭제
        cols[fx][fy] = False
    else:   # 보 삭제
        rows[fx][fy] = False

def check_frames(cols, rows, result):
    for x, y, a in result:
        # 기둥인 경우
        if a == 0:
            if y > 0 and (not rows[x-1][y] and not rows[x][y]) and not cols[x][y-1]:
                return False
        # 보인 경우
        else:
            if (not cols[x][y-1] and not cols[x+1][y-1]) and not (rows[x-1][y] and rows[x+1][y]):
                return False
    return True

def solution(n, build_frame):
    cols = [[False] * (n+1) for _ in range(n+1)]
    rows = [[False] * (n+1) for _ in range(n+1)]
    result = []
    
    for frame in build_frame:
        order = frame[3]
        # 삭제하는 경우
        if order == 0:
            del_frame(cols, rows, frame, result)
        # 설치하는 경우
        else:
            add_frame(cols, rows, frame, result)
            
        # 모든 프레임이 조건을 만족하지 못하면 해당 order 취소
        if not check_frames(cols, rows, result):
            # 삭제 취소
            if order == 0:
                add_frame(cols, rows, frame, result)
            # 설치 취소
            else:
                del_frame(cols, rows, frame, result)
    
    result.sort(key = lambda x : (x[0], x[1], x[2]))
    return result