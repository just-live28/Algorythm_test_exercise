# 2_index, 3_index, 5_index = 0, 0, 0
# (1) 3개의 index 중 가장 작은 것을 하나 올린다.
# (2) 모든 인덱스

n = int(input())
ugly = [0] * n
ugly[0] = 1
idx_2, idx_3, idx_5 = 0, 0, 0
next_2, next_3, next_5 = 2, 3, 5
for i in range(1, n):
    ugly[i] = min(next_2, next_3, next_5)
    
    if ugly[i] == next_2:
        idx_2 += 1
        next_2 = ugly[idx_2] * 2
    if ugly[i] == next_3:
        idx_3 += 1
        next_3 = ugly[idx_3] * 3
    if ugly[i] == next_5:
        idx_5 += 1
        next_5 = ugly[idx_5] * 5

print(ugly)
print(ugly[n-1])