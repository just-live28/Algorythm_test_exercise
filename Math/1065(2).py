n = int(input())

if n < 100:
    print(n)
else:
    count = 99
    for num in range(100, n+1):
        if num == 1000:
            continue
        num = str(num)
        if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
            count += 1
    print(count)