import sys
input = sys.stdin.readline

n = int(input())
tasks = []
for _ in range(n):
    st, en = map(int, input().split())
    tasks.append((st, en))
tasks.sort(key = lambda x : (x[1], x[0]))

count = 1
last_end = tasks[0][1]
for i in range(1, n):
    st, en = tasks[i]
    
    if st >= last_end:
        count += 1
        last_end = en

print(count)