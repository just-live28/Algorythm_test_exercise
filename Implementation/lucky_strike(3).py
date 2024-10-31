# n을 반으로 나눈다 / 왼쪽 합/ 오른쪽 합이 동일하면 발동

n = input()
length = len(n) // 2

left = n[:length]
right = n[length:]

left_score = 0
right_score = 0
for i in range(length):
    left_score += int(left[i])
    right_score += int(right[i])

if left_score == right_score:
    print("LUCKY")
else:
    print("READY")