import copy
from itertools import permutations

def solution(n, weak, dist):
    W = len(weak)
    F = len(dist)
    
    weaks = copy.deepcopy(weak)
    for i in weak:
        weaks.append(n + i)
    
    result = F + 1
    for st in range(W):
        for friends in permutations(dist, F):
            count = 1
            fidx = 0
            widx = st
            cover = weaks[widx] + friends[fidx]
            widx += 1
            
            while True:
                if count == W:
                    result = min(result, fidx + 1)
                    break
                
                if weaks[widx] <= cover:
                    count += 1
                    widx += 1
                else:
                    fidx += 1
                    if fidx == F:
                        break
                    else:
                        count += 1
                        cover = weaks[widx] + friends[fidx]
                        widx += 1
    
    if result == F + 1:
        return -1
    else:
        return result