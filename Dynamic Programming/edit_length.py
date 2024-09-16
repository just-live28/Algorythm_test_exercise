str_a = input()
str_b = input()

# a 97 z 122
arr_a = [0] * 123
arr_b = [0] * 123

for i in str_a:
    arr_a[ord(i)] += 1

for i in str_b:
    arr_b[ord(i)] += 1

a_only = 0
b_only = 0
for i in range(97,123):
    if arr_a[i] > arr_b[i]:
        a_only += arr_a[i] - arr_b[i]
    elif arr_a[i] < arr_b[i]:
        b_only += arr_b[i] - arr_a[i]

print(b_only)

