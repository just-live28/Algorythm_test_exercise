import copy
from collections import deque

cases = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def flip(array, numbers):
    newArray = copy.deepcopy(array)
    for number in numbers:
        if newArray[number] == '1':
            newArray[number] = '0'
        else:
            newArray[number] = '1'
    return newArray

def cal_min_flip(board):
    visited = [False] * 512
    initBinValue = int(''.join(board), 2)
    visited[initBinValue] = True
    
    q = deque()
    q.append((initBinValue, 0))
    
    while q:
        binValue, count = q.popleft()
        # 모든 칸의 동전이 앞면 또는 뒷면인 경우 뒤집은 횟수를 반환
        if binValue == 0 or binValue == 511:
            return count
        # 상태값을 9자리 배열로 변환 후 각 경우에 따라 뒤집기
        binArray = list(bin(binValue)[2:].zfill(9))
        for case in cases:
            flippedBinArray = flip(binArray, case)
            flippedBinValue = int(''.join(flippedBinArray), 2)
            # 아직 해 본 적 없는 경우라면 방문 처리 후 뒤집은 횟수를 증가시켜 큐에 추가
            if not visited[flippedBinValue]:
                visited[flippedBinValue] = True
                q.append((flippedBinValue, count + 1))
                
    return -1

tc = int(input())
for _ in range(tc):
    board = []
    for _ in range(3):
        line = list(input().split())
        for i in range(3):
            if line[i] == 'H':
                board.append('1')
            else:
                board.append('0')
                
    print(cal_min_flip(board))