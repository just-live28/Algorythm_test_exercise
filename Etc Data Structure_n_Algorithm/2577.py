a = int(input())
b = int(input())
c = int(input())
result = a * b * c
table = [0] * 10
while result != 0:
    table[result % 10] += 1
    result //= 10

for i in table:
    print(i)