import copy
from itertools import permutations

def solution(n, weak, dist):
    w = len(weak)
    nweak = copy.deepcopy(weak)
    
    for each_weak in weak:
        nweak.append(each_weak + n)
    
    min_friend = len(dist) + 1
    for start in range(w):
        for friends in permutations(dist, len(dist)):
            coverage = nweak[start] + friends[0]
            fcount = 1
            check = 1
            
            while True:
                if check == w:
                    min_friend = min(min_friend, fcount)
                    break
                
                if nweak[start + check] > coverage:
                    if fcount == len(dist):
                        break
                    else:
                        coverage = nweak[start + check] + friends[fcount]
                        check += 1
                        fcount += 1
                else:
                    check += 1
    
    if min_friend == len(dist) + 1:
        return -1
    else:
        return min_friend