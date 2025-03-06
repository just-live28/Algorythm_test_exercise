# a 1~100만. 중복 없음. 중복 선택 불가
# a(i) + a(j) = x를 만족하는 (ai, aj) 쌍의 수 구하기

# 해시 테이블에 x - ai 를 저장해두고
# aj를 키로 그 값이 있는지를 확인한다.


n = int(input())
arr = list(map(int, input().split()))
x = int(input())

dic = {}
for i in arr:
    if x-(x-i) not in dic:
        dic[x-i] = 1

count = 0
for i in arr:
    if x == 2 * i:
        continue
    if i in dic:
        count += 1
print(count)