import sys
input = sys.stdin.readline

data = [None] * 600001
prev = [-1] * 600001
next = [-1] * 600001
unused = 1

def insert(addr, c):
    global unused
    data[unused] = c
    
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

def traverse():
    current = next[0]
    while current != -1:
        print(data[current], end='')
        current = next[current]
    
string = input().rstrip()
cursor = 0
for i in range(len(string)):
    insert(i, string[i])
    cursor += 1

m = int(input())
for _ in range(m):
    line = input().rstrip().split()
    if len(line) == 2:
        insert(cursor, line[1])
        cursor = next[cursor]
    elif line[0] == 'L' and prev[cursor] != -1:
        cursor = prev[cursor]
    elif line[0] == 'D' and next[cursor] != -1:
        cursor = next[cursor]
    elif line[0] == 'B':
        if prev[cursor] != -1:
            erase(cursor)
            cursor = prev[cursor]

traverse()