# 1 ~ 1000000

# 0~9까지 가장 많은 숫자가 세트가됨
# 단, 6과 9는 둘이 합쳐서 2로 나눠야 함.
import math

n = int(input())
table = [0] * 10
while n != 0:
    table[n % 10] += 1
    n //= 10

temp = math.ceil((table[6] + table[9]) / 2)
table[6] = temp
table[9] = temp
print(max(table))