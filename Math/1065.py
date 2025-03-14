# 양의 정수 X 각 자리가 등차수열인 수 -> 한수
# 등차수열 : 3 5 7

# 1 ~ N 까지 수 중 한수를 출력
# 한자릿수: 전부 
# 두자릿수: 전부
# 세자릿수: 1~2자리 차, 2~3 차가 동일해야 함.

n = int(input())
count = 0
for i in range(1, n+1):
    if i < 100:
        count += 1
    else:
        number = str(i)
        if int(number[0]) - int(number[1]) == int(number[1]) - int(number[2]):
            count += 1

print(count)