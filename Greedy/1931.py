# n개의 회의에 대해 한개의 회의실을 배정. 가장 많은 회의를 진행할 수 있게
# 끝남과 동시에 새로 회의 시작 가능
# 가능한 한 알차게 배치

# 시작시간이 빠른 순서로 -> (0 23) (1 2) (2 3)...이 있다면 0 23이 먼저 회의실을 써서 최대 회의 개수 불가
# 종료시간이 빠른 순서로 -> 빨리 끝나는 대로 넣되, 시작 시간이 이전 게 끝나는 시간보다 같거나 이후여야 한다.

n = int(input())
tasks = []
for _ in range(n):
    a, b = map(int, input().split())
    tasks.append((a, b))
tasks.sort(key = lambda x : (x[1], x[0]))

count = 0
prev_end = 0
for start, end in tasks:
    if start >= prev_end:
        count += 1
        prev_end = end

print(count)