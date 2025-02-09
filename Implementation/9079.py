import copy
from collections import deque

cases = [(0,3,6), (1,4,7), (2,5,8), (0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6)]

def flip(numbers, arr):
    new_arr = copy.deepcopy(arr)
    for i in numbers:
        if new_arr[i] == '1':
            new_arr[i] = '0'
        else:
            new_arr[i] = '1'
    return int(''.join(new_arr), 2)

def solution(binValue):
    if binValue == 0 or binValue == 511:
        return 0
    
    visited = [False] * 512
    visited[binValue] = True
    
    q = deque()
    binArr = list(bin(binValue)[2:].zfill(9))
    q.append((binArr, 0))
    
    while q:
        arr, count = q.popleft()
        
        for numbers in cases:
            flippedBinValue = flip(numbers, arr)
            if flippedBinValue == 0 or flippedBinValue == 511:
                return count + 1
            if not visited[flippedBinValue]:
                visited[flippedBinValue] = True
                flippedBinArr = list(bin(flippedBinValue)[2:].zfill(9))
                q.append((flippedBinArr, count + 1))
    
    return -1

tc = int(input())
for _ in range(tc):
    board = []
    for _ in range(3):
        for i in input().split():
            if i == 'H':
                board.append('1')
            else:
                board.append('0')

    print(solution(int(''.join(board), 2)))