# 하루에 a - b만큼 올라간다.
# 단, 낮에 정상에 올라갔다면 끝. 미끄러지지 않음.
# 언제까지? v-a의 높이까지(넘어도 상관없음) -> ceil((v-a) / (a-b))
# 그 뒤, + 1을 하면 됨.
import math

a, b, v = map(int, input().split())
print(math.ceil((v-a) / (a-b)) + 1)