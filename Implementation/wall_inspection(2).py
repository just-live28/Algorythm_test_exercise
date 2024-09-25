# 각 취약점 별로 시작한다.
# 1명만 쓰는 경우, 2명만 쓰는 경우, 3명만 쓰는 경우, 4명 다 쓰는 경우의 [순열]
# 첫 친구를 취약점에 투입
# 다음 취약점을 이 친구가 커버하면 또 다음 취약점으로
# 커버 못하는 취약점에 또 다른 친구를 투입
# 더이상 친구가 없다면 / 모든 친구를 써도 끝 취약점에 도달하지 못한다면 --> continue
# 모든 취약점 점검에 성공한다면 --> is_possilbe = True 이고 min_friends가 최소라면 갱신
# 모든 경우의 수에 대해 검사한 후 is_possible이 False라면 -1반환

from itertools import permutations

def solution(n, weak, dist):
    
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    
    min_friends = len(dist) + 1
    #각 취약 지점 별로 시작
    for start in range(length):
        #친구들의 조합(friends)
        for friends in list(permutations(dist, len(dist))):
            count = 1
            #점검 가능한 마지막 위치
            position = weak[start] + friends[count-1]
            #시작점부터 모든 취약점 확인
            for i in range(start, start + length):
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i] + friends[count-1]
            min_friends = min(min_friends, count)
    
    if min_friends > len(dist):
        return -1
    return min_friends  