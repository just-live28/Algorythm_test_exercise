n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
last_time = 0
for i in range(n):
    result += last_time + arr[i]
    last_time += arr[i]

print(result)