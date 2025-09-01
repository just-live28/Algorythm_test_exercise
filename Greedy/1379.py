# N개의 강의 / 시작, 끝 시간 / 최대한 적은 수의 강의실로 모든 강의가 이루어지게
# 빨리빨리 시작해야 한다, 기다릴 수 없음. 시작 시간에는 강의가 시작해야 함.
# 가장 간단한 해결책은 강의마다 한 강의실을 쓰는 것 -> 최대한 많은 수
# 현재 열린 강의실 중 끝난 게 있다면, 거기 새 강의를 넣는 게 가장 적은 수의 강의실을 만들 수 있음
# 힙큐를 사용하면, 가장 빨리 끝나는 강의실 시간을 알 수 있고, 나머지는 이것보다 더 늦게 끝나므로, 이것보다도 시작시간이 작으면 모든 강의실에 들어갈 수 없음.
# 결론: 시작 시간, 끝 시간 순으로 정렬

import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    num, st, en = map(int, input().split())
    arr.append((st, en, num))
arr.sort()

count = 0
# (en, idx)
classrooms = []
match_info = [0] * (n+1)
for i in range(n):
    st, en, num = arr[i]
    
    if classrooms and st >= classrooms[0][0]:
        _, idx = heapq.heappop(classrooms)
        heapq.heappush(classrooms, (en, idx))
        match_info[num] = idx
    else:
        count += 1
        heapq.heappush(classrooms, (en, count))
        match_info[num] = count

print(count)
for i in range(1, n+1):
    print(match_info[i])