# - 로 덩어리 나누고, 덩어리마다 +로 나눈 다음 2개 이상이면 합하기. 그리고 처음 거에서 다 빼버리기
line = input().split('-')

for i in range(len(line)):
    each = line[i].split('+')
    if len(each) == 1:
        line[i] = int(each[0])
    else:
        line[i] = sum([int(x) for x in each])
    
if len(line) == 1:
    print(line[0])
else:
    print(line[0] - sum(line[1:]))