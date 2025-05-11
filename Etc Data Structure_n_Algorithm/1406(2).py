import sys
input = sys.stdin.readline

data = [0] * 600001
pre = [-1] * 600001
nxt = [-1] * 600001
unused = 1

def insert(addr, item):
    global unused
    
    data[unused] = item
    pre[unused] = addr
    nxt[unused] = nxt[addr]
    
    if nxt[addr] != -1:
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    
    unused += 1

def erase(addr):
    nxt[pre[addr]] = nxt[addr]
    
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]

def traversal():
    cur = nxt[0]
    
    while cur != -1:
        print(data[cur], end='')
        cur = nxt[cur]
    print()

init_str = input().rstrip()
n = len(init_str)
cur = 0
for i in range(n):
    insert(cur, init_str[i])
    cur = nxt[cur]

m = int(input())
for _ in range(m):
    line = list(input().rstrip().split())
    
    if len(line) == 1:
        if line[0] == 'L' and pre[cur] != -1:
            cur = pre[cur]
        elif line[0] == 'D' and nxt[cur] != -1:
            cur = nxt[cur]
        elif line[0] == 'B' and pre[cur] != -1:
            erase(cur)
            cur = pre[cur]
    else:
        insert(cur, line[1])
        cur = nxt[cur]

traversal()