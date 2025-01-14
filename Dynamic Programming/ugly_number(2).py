# 인덱스를 통해 관리
# d[n] = min(next_2, next_3, next_5)
# 선택되면 해당하는 수에 대한 index를 하나 늘린 후 그 수에 해당 수를 곱하여 next를 갱신한다.
# index_2 = 0일 때 2가 선택되었다 치면 index_2 = 1이 되고, ugly[index_2] * 2가 next_2가 된다.

i2 = i3 = i5 = 0

next_2, next_3, next_5 = 2, 3, 5

n = int(input())

ugly = [0] * n
ugly[0] = 1

for i in range(1, n):
    ugly[i] = min(next_2, next_3, next_5)
    
    if ugly[i] == next_2:
        i2 += 1
        next_2 = ugly[i2] * 2
    if ugly[i] == next_3:
        i3 += 1
        next_3 = ugly[i3] * 3
    if ugly[i] == next_5:
        i5 += 1
        next_5 = ugly[i5] * 5

print(ugly[n-1])
print(ugly)