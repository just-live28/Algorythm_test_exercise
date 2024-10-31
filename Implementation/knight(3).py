# print(ord('a')) 97

loc = input()

x, y = int(loc[1]), ord(loc[0]) - 96

# 1~8 / 1~8 board

moves = [(1, 2), (1, -2), (2, -1), (2, 1), (-1, 2), (-1, -2), (-2, -1), (-2, 1)]

result = 0
for dx, dy in moves:
    nx, ny = x + dx, y + dy

    if 1 <= nx and nx <= 8 and 1 <= ny and ny <= 8:
        result += 1

print(result)