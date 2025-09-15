a, b = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = set(map(int, input().split()))

result = []
for num in arr_a:
    if num not in arr_b:
        result.append(num)

if not result:
    print(0)
else:
    print(len(result))
    result.sort()
    print(*result)