## ord(알파벳) - 96

loc = input()
x = ord(loc[0]) - 96
y = int(loc[1])

moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

count = 0
for move in moves:
    nx, ny = x + move[0], y + move[1]
    
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)