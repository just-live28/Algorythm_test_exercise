from collections import deque

def push_front(x):
    q.appendleft(x)
    
def push_back(x):
    q.append(x)
    
def pop_front():
    if q:
        return q.popleft()
    return -1

def pop_back():
    if q:
        return q.pop()
    return -1

def size():
    return len(q)
    
def empty():
    if len(q) == 0:
        return 1
    return 0

def front():
    if q:
        return q[0]
    return -1

def back():
    if q:
        return q[-1]
    return -1

q = deque()
n = int(input())
for _ in range(n):
    line = input().split()
    
    if line[0] == 'push_back':
        push_back(line[1])
    elif line[0] == 'push_front':
        push_front(line[1])
    elif line[0] == 'pop_back':
        print(pop_back())
    elif line[0] == 'pop_front':
        print(pop_front())
    elif line[0] == 'size':
        print(size())
    elif line[0] == 'empty':
        print(empty())
    elif line[0] == 'front':
        print(front())
    elif line[0] == 'back':
        print(back())