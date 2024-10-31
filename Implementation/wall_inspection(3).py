from itertools import permutations
INF = int(1e9)

weak = [1,3,4,9,10]
dist = [3,5,7]
n = 12

# def solution(n, weak, dist):
#     answer = 0
#     return answer

length = len(weak)

for i in range(length):
    weak.append(weak[i] + n)

# [1, 5, 6, 10, 13, 17, 18, 22]
min_result = INF
for start in range(length):
    for friends in permutations(dist, len(dist)):
        wall_count = 1
        friend_count = 1
        cover = weak[start] + friends[0]
        
        while True:
            if wall_count == length:
                break
            
            if weak[start + wall_count] <= cover:
                wall_count += 1
                continue
            
            if friend_count == len(dist):
                friend_count = INF
                break
            else:
                cover = weak[start + wall_count] + friends[friend_count]
                friend_count += 1
                wall_count += 1

        if friend_count < min_result:
            min_result = friend_count

if min_result == INF:
    print(-1)
else:
    print(min_result)