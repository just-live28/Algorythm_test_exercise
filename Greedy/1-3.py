numbers = input()

count_0 = 0
count_1 = 0
prev = int(numbers[0])
for i in range(1, len(numbers)):
    target = int(numbers[i])
    if target != prev:
        if prev == 0:
            count_0 += 1
        else:
            count_1 += 1
        prev = target
        
if int(numbers[-1]) == 0:
    count_0 += 1
else:
    count_1 += 1

print(min(count_0, count_1))