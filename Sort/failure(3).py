def solution(N, stages):
    count = [0] * (N+2)
    for stage in stages:
        count[stage] += 1

    failures = []
    for i in range(1, len(count)-1):
        # i탄 실패율 = i탄의 수 / (i탄 수 + i탄 이상 간 수)
        if count[i] == 0:
            failures.append((i, 0))
        else:
            success_players = 0
            for j in range(i + 1, len(count)):
                success_players += count[j]
            
            failure = count[i] / (count[i] + success_players)
            failures.append((i, failure))

    failures.sort(key = lambda x : (-x[1], x[0]))

    result = []
    for i in range(len(failures)):
        result.append(failures[i][0])
    
    return result

# 실패율 : 도달했으나 클리어 못한 수 / 도달한 수 (도달한 사람 + 이 스테이지 이상 깬 사람)
# 현재 멈춰있는 스테이지 번호.(도달했으나 클리어 못한 스테이지)
