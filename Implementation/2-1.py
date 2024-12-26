n = input()

unit = len(n) // 2
left_side = sum([int(x) for x in n[:unit]])
right_side = sum([int(x) for x in n[unit:]])

if left_side == right_side:
    print("LUCKY")
else:
    print("READY")