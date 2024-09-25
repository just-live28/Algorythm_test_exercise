# 기둥(아래좌표 기준) ↑ : 바닥 위 / 보의 한쪽 끝부분 위 / 다른 기둥 위
# 보(왼쪽좌표기준) ← : 한쪽 끝부분이 기둥 위 / 양쪽 끝부분이 다른 보와 동시에 연결

# 설치) 해당 구조물 추가 후 check. 불만족 시 다시 제거
# 제거) 해당 구조물 제거 후 check. 불만족 시 다시 추가

# [x, y, a, b] : x좌표 / y좌표 / 0 기둥 1 보 / 0 삭제 1 설치

# pillars[a][b] = boolean (a,b) 좌표 기준의 기둥이 존재하는지
# beams[a][b] = boolean (a,b) 좌표 기준의 보가 존재하는지

# 어느 쪽 교차점 기준인지 정확히 파악
# 문제의 조건에 명시되어 있는 입력값의 불필요한 조건 검사 지양

frames = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]


def check(array, pillars, beams):
    for frame in array:
        x, y, type = frame
        # 기둥일 때
        if type == 0:
            if y != 0 and not(beams[x-1][y] == True or beams[x][y] == True) and not(pillars[x][y-1] == True):
                return False
        # 보일 때
        else:
            if not(pillars[x][y-1] == True or pillars[x+1][y-1] == True) and not(beams[x-1][y] == True and beams[x+1][y] == True):
                return False
    return True

def solution(n, build_frame):
    pillars = [[False]*(n+1) for _ in range(n+1)]
    beams = [[False]*(n+1) for _ in range(n+1)]
    result = []
    
    for frame in build_frame:
        x, y, type, option = frame
        
        #삭제
        if option == 0:
            result.remove([x, y, type])
            if type == 0:
                pillars[x][y] = False
            else:
                beams[x][y] = False
                
            if check(result, pillars, beams) == False:
                result.append([x,y,type])
                if type == 0:
                    pillars[x][y] = True
                else:
                    beams[x][y] = True
        #추가
        else:
            result.append([x,y,type])
            if type == 0:
                pillars[x][y] = True
            else:
                beams[x][y] = True
            
            if check(result, pillars, beams) == False:
                result.pop()
                if type == 0:
                    pillars[x][y] = False
                else:
                    beams[x][y] = False
        
    result.sort(key = lambda x : (x[0], x[1], x[2]) )
    return result

print(solution(5, frames))