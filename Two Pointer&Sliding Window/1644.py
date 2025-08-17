n = int(input())

eratos = [True] * (n+1)
i = 2
while i * i <= n:
    if not eratos[i]:
        i += 1
        continue
    
    cur = i * i
    while cur <= n:
        eratos[cur] = False
        cur += i
    i += 1

arr = []
for i in range(2, n+1):
    if eratos[i]:
        arr.append(i)
arr_size = len(arr)

if n == 1:
    print(0)
else:
    result = 0
    en = 0
    total_sum = arr[0]
    for st in range(arr_size):
        while en < arr_size and total_sum < n:
            en += 1
            if en < arr_size:
                total_sum += arr[en]
        if en == n:
            break
        
        if total_sum == n:
            result += 1
        total_sum -= arr[st]

    print(result)