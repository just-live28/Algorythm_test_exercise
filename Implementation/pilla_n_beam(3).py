# def solution(n, build_frame):
#     answer = [[]]
#     return answer

# build_frame
# [x,y,a,b] : a) 0기둥 1보 / b) 0삭제 1설치

# result
# [x, y, 종류] 0기둥 1보

# x,y 기준) 기둥 : 아래쪽좌표 / 보 : 왼쪽좌표

# 규칙
# 기둥) 바닥 위 / 보 한쪽 끝부분 위 / 다른 기둥 위
# 보) 한쪽 끝이 기둥 위 / 양쪽 끝이 다른 보와 동시에 연결

def check(frames):
    for frame in frames:
        fx, fy, ftype = frame
        
        if ftype == 0: #기둥일 때
            if not fy == 0 and not ((fx-1, fy, 1) in frames or (fx, fy, 1) in frames) and not (fx, fy-1, 0) in frames:
                return False
        else: #보일 때
            if not ((fx, fy-1, 0) in frames or (fx+1, fy-1, 0) in frames) and not ((fx-1, fy, 1) in frames and (fx+1, fy, 1) in frames):
                return False
            
    return True

def solution(n, build_frame):
    result = []
    for order in build_frame:
        ox, oy, otype, option = order
        
        if option == 0: # 삭제하는 경우
            result.remove((ox, oy, otype))
            
            if check(result) == False:
                result.append((ox, oy, otype))
        else: # 추가하는 경우
            result.append((ox, oy, otype))
            
            if check(result) == False:
                result.remove((ox, oy, otype))
    
    result.sort(key = lambda x : (x[0], x[1], x[2]))
    return result