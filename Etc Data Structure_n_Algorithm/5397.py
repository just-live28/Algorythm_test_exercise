MX = 1000001

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

def traversal():
    cur = next[0]
    while cur != -1:
        print(data[cur], end='')
        cur = next[cur]
    print()

tc = int(input())
for _ in range(tc):
    unused = 1
    data = [None] * MX
    prev = [-1] * MX
    next = [-1] * MX
    cursor = 0
    line = input()
    for i in line:
        if i == '<':
            if prev[cursor] == -1:
                continue
            cursor = prev[cursor]
        elif i == '>':
            if next[cursor] == -1:
                continue
            cursor = next[cursor]
        elif i == '-':
            if prev[cursor] == -1:
                continue
            erase(cursor)
            cursor = prev[cursor]
        else:
            insert(cursor, i)
            cursor = next[cursor]
    traversal()