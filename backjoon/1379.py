import heapq
import sys
input = sys.stdin.readline

# (끝 시간, 강의실 번호)
n = int(input())
new_room = 1
room_class_match_table = [0] * 100001
classes = []
for _ in range(n):
    idx, st, en = map(int, input().rstrip().split())
    classes.append((idx, st, en))
classes.sort(key = lambda x : (x[1], x[2]))

q = []
heapq.heappush(q, (0, new_room))
for idx, st, en in classes:
    if st >= q[0][0]:
        _, r_idx = heapq.heappop(q)
        room_class_match_table[idx] = r_idx
        heapq.heappush(q, (en, r_idx))
    else:
        new_room += 1
        room_class_match_table[idx] = new_room
        heapq.heappush(q, (en, new_room))

print(new_room)
for i in room_class_match_table[1:n+1]:
    print(i)