from collections import deque

n, k = map(int, input().split())
array = [x for x in range(1, n+1)]

count = n
prev = 0
print('<', end='')
while count > 0:
    index = (prev + k - 1) % count
    
    if count == 1 :
        print(array.pop(index), end='>')
    else:
        print(array.pop(index), end=', ')
    
    count -= 1
    prev = index