# cur에 num을 더하면서, 몇 번째 라인인지 구하기
# num이 분모 + 분자
# 홀수번째(num이 짝수)면, 왼쪽이 1부터 시작
# 짝수번째(num이 홀수)면, 오른쪽이 1부터 시작

x = int(input())

cur = 0
num = 0
while cur < x:
    cur += num
    num += 1

if num % 2 == 0:
    left = 1 + (cur - x)
    right = num-1 - (cur - x)
else:
    right = 1 + (cur - x)
    left = num-1 - (cur - x)

print(left, end='')
print('/', end='')
print(right)