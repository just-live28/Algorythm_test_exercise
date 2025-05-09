n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = 0
remains = [0] * m
remains[0] += 1

for i in range(n):
    prefix_sum += arr[i]
    remains[prefix_sum % m] += 1

result = 0
for i in remains:
    result += (i * (i-1)) // 2

print(result)