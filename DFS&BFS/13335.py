from collections import deque

n, w, l = map(int, input().split())
arr = list(map(int, input().split()))

def move_trucks(trucks):
    global load

    for truck in trucks:
        truck[1] -= 1
        if truck[1] == 0:
            load -= truck[0]
    
    for truck in trucks:
        if truck[1] == 0:
            trucks.remove(truck)
            
q = deque(arr)

load = 0
total_time = 0
on_bridge = []
while q:
    total_time += 1
    move_trucks(on_bridge)

    if q[0] + load <= l:
        new = q.popleft()
        load += new
        on_bridge.append([new, w])
    
print(total_time + on_bridge[-1][1])