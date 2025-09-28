# 4 5
# GIBSON YYYNN
# FENDER YYNNY
# EPIPHONE NNNYY
# ESP YNNNN
from itertools import combinations

n, m = map(int, input().split())
guitars = []
for _ in range(n):
    name, songs = input().split()
    
    cur = 0
    for i in range(m-1, -1, -1):
        if songs[i] == 'Y':
            cur |= (1 << (m-i-1))
    
    guitars.append(cur)

max_songs = 0
result = 0
for size in range(1, n+1):
    for each in combinations(guitars, size):
        cur = 0
        for e in each:
            cur |= e
        
        if cur > max_songs:
            max_songs = cur
            result = size

if max_songs == 0:
    print(-1)
else:
    print(result)