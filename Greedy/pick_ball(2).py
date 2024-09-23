from itertools import combinations

# n 개수 m 최대 무게
n, m = map(int, input().split())
balls = list(map(int, input().split()))

# 순서 x 중복 x
# 조합 combinations

# 두 사람. <- 사람 간 구별이 없음. (2번공, 3번공) 과 (3번공, 2번공) 은 동일
# --> 전체 결과 값에서 2를 나눠야 함.

count = 0
for set in list(combinations(balls, 2)):
    if set[0] != set[1]:
        count += 1

print(count)

