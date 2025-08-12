# 문자, 숫자를 분리하여 각 리스트에 추가
# 문자 리스트는 정렬, 숫자 리스트는 합산
line = input()
alphas = []
sum = 0
for i in line:
    if i.isalpha():
        alphas.append(i)
    else:
        sum += int(i)
alphas.sort()

print(''.join(alphas) + str(sum))