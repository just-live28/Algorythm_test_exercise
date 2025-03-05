word = input()

dic = { 'c=': 1, 'c-': 1, 'dz=': 1, 'd-': 1, 'lj': 1, 'nj': 1, 's=': 1, 'z=': 1}

idx = 0
result = 0
while idx < len(word):
    if word[idx:idx+2] in dic:
        result += 1
        idx += 2
    elif word[idx:idx+3] in dic:
        result += 1
        idx += 3
    else:
        result += 1
        idx += 1
print(result)