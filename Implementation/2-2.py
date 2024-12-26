s = input()

numbers = [int(x) for x in s if x.isnumeric()]
strings = [x for x in s if x.isalpha()]

strings.sort()

for string in strings:
    print(string, end = '')

print(sum(numbers))