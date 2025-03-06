# 1~N 까지 원을 이루며 앉음. 
# K번째 사람을 제거

n, k = map(int, input().split())

MX = 5001
unused = 1
data = [None] * MX
prev = [-1] * MX
next = [-1] * MX

def insert(addr, x):
    global unused
    
    data[unused] = x
    prev[unused] = addr
    next[unused] = next[addr]
    
    if next[addr] != -1:
        prev[next[addr]] = unused
    next[addr] = unused
    
    unused += 1

def erase(addr):
    next[prev[addr]] = next[addr]
    if next[addr] != -1:
        prev[next[addr]] = prev[addr]

def find_target(t):
    global cur
    for _ in range(t):
        cur = next[cur]
        if cur == -1:
            cur = next[0]
    return cur

cur = 0
for i in range(1, n+1):
    insert(cur, i)
    cur += 1
cur = 0
print('<', end='')
for i in range(n):
    target = find_target(k)
    if i == n-1:
        print(target, end='')
    else:
        print(target, end=', ')
    erase(target)
    cur = prev[cur]
print('>')