# 음수끼리 스플릿
# 각 스플릿에 대해 양수로 스플릿 후 합치기
# 첫 요소 - 나머지 요소의 합 으로 답 구하기

line = input().split('-')
result = sum([int(x) for x in line[0].split('+')])

if len(line) > 1:
    for each in line[1:]:
        result -= sum([int(x) for x in each.split('+')])
    
print(result)