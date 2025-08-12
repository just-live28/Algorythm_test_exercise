# 반으로 갈라서 좌우 합을 비교하기
# 좌우 합이 같다면, LUCKY 다르다면 READY

line = [int(x) for x in input()]
mid = len(line) // 2
if sum(line[:mid]) == sum(line[mid:]):
    print("LUCKY")
else:
    print("READY")