import sys
input = sys.stdin.readline

n = int(input())
arr = []
count = [0] * 8001  # n - 4000
for _ in range(n):
    num = int(input())
    arr.append(num)
    count[num + 4000] += 1
arr.sort()

print(round(sum(arr) / n))
print(arr[n // 2])

result = []
max_freq = 0
for i in range(8001):
    if count[i] == 0:
        continue
    if count[i] > max_freq:
        max_freq = count[i]
        result.clear()
        result.append(i-4000)
    elif count[i] == max_freq:
        result.append(i-4000)
if len(result) > 1:
    print(result[1])
else:
    print(result[0])

print(arr[-1] - arr[0])