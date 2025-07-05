n = int(input())
m = int(input())
orders = list(map(int, input().split()))

def find_frame_idx(frames, number):
    for i in range(len(frames)):
        if frames[i][2] == number:
            return i
    return -1

frames = []
like_table = [0] * 101

for j in range(m):
    num = orders[j]
    frame_idx = find_frame_idx(frames, num)

    if len(frames) < n and frame_idx != -1:
        frames[frame_idx][0] += 1
        like_table[num] += 1
    elif len(frames) < n and frame_idx == -1:
        frames.append([1, j, num])
        like_table[num]
    elif len(frames) == n and frame_idx != -1:
        frames[frame_idx][0] += 1
        like_table[num] += 1
    elif len(frames) == n and frame_idx == -1:
        frames.sort(key = lambda x : (-x[0], -x[1]))
        evict = frames.pop()
        like_table[evict[2]] = 0

        frames.append([1, j, num])
        like_table[num] = 1

result = []
for i in range(1, 101):
    if like_table[i] > 0:
        result.append(i)

print(*result)