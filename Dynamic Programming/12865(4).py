# knapsack problem (0-1)
# 각 물건은 무게 w, 가치 v
# 최대 k 무게를 넣을 수 있는 배낭 안의 물건 가치의 최댓값

# d[wgt] = 배낭의 무게가 wgt일 때, 가치의 최댓값 (단 wgt <= k)

# 뒤에서부터 역순으로 wgt를 검사. wgt - w >= 0일 때까지 (앞에서부터 검사 시 같은 물건이 중복될 수 있음)
# d[wgt] = max(d[wgt], d[wgt - w] + v)
# 초깃값. d[w] = v

n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(map(int, input().split()))

d = [0] * (k+1)
for i in range(n):
    w, v = arr[i]
    for wgt in range(k, -1, -1):
        if wgt - w < 0:
            break
        d[wgt] = max(d[wgt], d[wgt - w] + v)

print(max(d))