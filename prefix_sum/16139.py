import sys
input = sys.stdin.readline

word = input().rstrip()
n = len(word)
d = [[0] * 26 for _ in range(n)]

for i in range(n):
    ch = word[i]
    for j in range(26):
        d[i][j] = d[i-1][j]
        if ord(ch) - 97 == j:
            d[i][j] += 1

q = int(input())
for _ in range(q):
    target, st, en = input().rstrip().split()
    target = ord(target) - 97
    st = int(st)
    en = int(en)
    
    if st == 0:
        print(d[en][target])
    else:
        print(d[en][target] - d[st-1][target])