str = input()

length = len(str) // 2
left = sum(list(map(int, str[:length])))
right = sum(list(map(int, str[length:])))

if left == right:
    print("LUCKY")
else:
    print("READY")