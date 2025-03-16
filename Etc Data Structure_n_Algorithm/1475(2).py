# 0~9 사이의 숫자가 한 세트
# 방 번호 구성에 몇 세트가 필요한지?
# 계수 정렬 후, 6에는 ceil((6+9)/2) 을 저장, 9는 0을 저장
# 리스트에서 가장 많은 값 출력
import math

number = input()
table = [0] * 10
for i in number:
    table[int(i)] += 1

table[6] = math.ceil((table[6] + table[9]) / 2)
table[9] = 0

print(max(table))