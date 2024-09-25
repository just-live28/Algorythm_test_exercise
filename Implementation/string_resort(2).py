import math

string = input()

chars = []
nums = []
for i in string:
    if i.isdigit():
        nums.append(int(i))
    else:
        chars.append(i)

chars.sort()

print(''.join(chars) + str(sum(nums)))
        