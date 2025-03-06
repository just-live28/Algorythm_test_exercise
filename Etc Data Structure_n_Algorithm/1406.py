import sys
input = sys.stdin.readline

MX = 600001 # 문제의 최대 크기에 맞춰 조절

unused = 1
data = [None] * MX
prev = [-1] * MX
next = [-1] * MX

def insert(addr, num):
    global unused
    data[unused] = num
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

cursor = 0
word = input().rstrip()
for i in word:
    insert(cursor, i)
    cursor += 1
m = int(input())
for _ in range(m):
    oper = input().rstrip().split()
    if len(oper) == 2:
        insert(cursor, oper[1])
        cursor = next[cursor]
    elif oper[0] == 'L':
        if prev[cursor] != -1:
            cursor = prev[cursor]
    elif oper[0] == 'D':
        if next[cursor] != -1:
            cursor = next[cursor]
    else:
        if prev[cursor] == -1:
            continue
        erase(cursor)
        cursor = prev[cursor]

traversal()