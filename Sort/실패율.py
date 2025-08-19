def solution(N, stages):
    cnt = [0] * (N+2)
    for stage in stages:
        cnt[stage] += 1
    
    result = []
    cur_user = len(stages)
    for i in range(1, N+1):
        if cnt[i] == 0:
            failure = 0
        else:
            failure = cnt[i] / cur_user
        cur_user -= cnt[i]
        result.append((i, failure))
    result.sort(key = lambda x : (-x[1], x[0]))
    
    return [x[0] for x in result]