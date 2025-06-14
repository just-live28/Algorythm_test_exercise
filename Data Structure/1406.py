import sys
input = sys.stdin.readline

data = [None] * 600001
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

def delete(addr):
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]

def traverse():
    current = nxt[0]
    while current != -1:
        print(data[current], end='')
        current = nxt[current]

cur = 0
word = input().rstrip()
for i in word:
    insert(cur, i)
    cur += 1

n = int(input())
for _ in range(n):
    line = input().rstrip().split()

    if line[0] == 'L' and pre[cur] != -1:
        cur = pre[cur]
    elif line[0] == 'D' and nxt[cur] != -1:
        cur = nxt[cur]
    elif line[0] == 'B':
        if pre[cur] != -1:
            delete(cur)
            cur = pre[cur]
    elif line[0] == 'P':
        insert(cur, line[1])
        cur = nxt[cur]

traverse()