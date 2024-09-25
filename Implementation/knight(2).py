string = input()

x = ord(string[0]) - 97
y = int(string[1]) - 1

moves = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

result = []
for move in moves:
    nx = x + move[0]
    ny = y + move[1]
    
    if 0 <= nx and nx < 8 and 0 <= ny and ny < 8:
        row = chr(nx + 97) 
        col = (ny+1)
        result.append(row + str(col))

for i in result:
    print(i, end=' ')