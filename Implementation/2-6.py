def check_frames(result):
    for fx, fy, ftype in result:
        # 기둥일 때
        if ftype == 0:
            if (not (fy == 0) and not ((fx, fy, 1) in result) and not ((fx-1, fy, 1) in result) and
            not ((fx, fy-1, 0) in result)):
                return False
        # 보일 때
        else:
            if (not ((fx, fy-1, 0) in result) and not ((fx+1, fy-1, 0) in result) and
            not ((fx-1, fy, 1) in result and (fx+1, fy, 1) in result)):
                return False
    return True
            
def solution(n, build_frame):
    result = []
    for fx, fy, ftype, fwork in build_frame:
        if fwork == 1:
            result.append((fx, fy, ftype))
        else:
            result.remove((fx, fy, ftype))
        
        if check_frames(result) == False:
            if fwork == 1:
                result.remove((fx, fy, ftype))
            else:
                result.append((fx, fy, ftype))
    
    result.sort(key = lambda x : (x[0], x[1], x[2]))
    return result