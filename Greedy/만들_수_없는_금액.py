# N개의 동전
# 양의 정수 금액 중, 만들 수 없는 최솟값
# 작은 순 정렬
# 해당 차례 coin이 현재 만들수 있는 값보다 크다면, 끝
# 아니라면 해당 coin 값을 현재 만들 수 있는 값에 합산

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

result = 1
for coin in coins:
    if result < coin:
        break
    result += coin

print(result)