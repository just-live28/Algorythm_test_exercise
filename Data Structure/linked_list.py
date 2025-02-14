data = [-1] * 100001
prev = [-1] * 100001
next = [-1] * 100001
unused = 6

data[1], data[2], data[4], data[5] = 65, 13, 21, 17
prev[1], prev[2], prev[4], prev[5] = 2, 0, 1, 4
next[0], next[1], next[2], next[4] = 2, 4, 1, 5

def traverse():
    current = next[0]
    while current != -1:
        print(data[current], end=' ')
        current = next[current]
    print()
        
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

insert(1, 99)
erase(6)
traverse()