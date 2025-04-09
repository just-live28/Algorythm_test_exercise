line = input()
str_arr = []
int_sum = 0

for i in line:
    if i.isnumeric():
        int_sum += int(i)
    else:
        str_arr.append(i)
str_arr.sort()

print(''.join(str_arr) + str(int_sum))