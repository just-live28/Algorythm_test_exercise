import sys
input = sys.stdin.readline

data = [None] * 600001
prev = [-1] * 600001
next = [-1] * 600001
unused = 1

def insert(addr, s):
    global unused
    data[unused] = s
    
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
    current = next[0]
    while current != -1:
        print(data[current], end='')
        current = next[current]
    print()

word = input().rstrip()
cursor = 0
for w in word:
    insert(cursor, w)
    cursor += 1

m = int(input())
for _ in range(m):
    cmd = input().rstrip().split()
    
    if len(cmd) == 2:
        insert(cursor, cmd[1])
        cursor = next[cursor]
    elif cmd[0] == 'L' and prev[cursor] != -1:
        cursor = prev[cursor]
    elif cmd[0] == 'D' and next[cursor] != -1:
        cursor = next[cursor]
    elif cmd[0] == 'B' and prev[cursor] != -1:
        erase(cursor)
        cursor = prev[cursor]

traversal()