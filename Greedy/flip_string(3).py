s = input()

group_0 = 0
group_1 = 0

prev = int(s[0])
for i in range(1, len(s)):
    number = int(s[i])
    if number != prev:
        if prev == 0:
            group_0 += 1
        else:
            group_1 += 1
        prev = number

if int(s[-1]) == 0:
    group_0 += 1
else:
    group_1 += 1

print(min(group_0, group_1))