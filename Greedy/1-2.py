# result가 0인 경우(첫 숫자) : 무조건 더하기
# 이외의 경우 : 0, 1인 경우 더하기 / 2~9인 경우 곱하기
num = input()

result = 0
for i in range(len(num)):
    if result == 0:
        result += int(num[i])
    else:
        target = int(num[i])
        if 0 <= target <= 1:
            result += target
        else:
            result *= target

print(result)