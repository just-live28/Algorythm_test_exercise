n = int(input())
positive = []
negative = []
for _ in range(n):
    num = int(input())
    if num > 0:
        positive.append(num)
    else:
        negative.append(-num)
positive.sort()
negative.sort()

result = 0
while positive:
    n1 = positive.pop()
    if positive:
        n2 = positive.pop()
        if n1 == 1 or n2 == 1:
            result += n1 + n2
        else:
            result += n1 * n2
    else:
        result += n1

while negative:
    n1 = negative.pop() * (-1)
    if negative:
        n2 = negative.pop() * (-1)
        result += n1 * n2
    else:
        result += n1

print(result)