x, y, z = map(int, input().split())
n = int(input())
inventory = [0] * n
for _ in range(n):
    a, b = map(int, input().split())
    inventory[a] = b

enable = True
count = 0
def fill_box(x_remain, y_remain, z_remain):
    global enable, count
    for i in range(n-1, -1, -1):
        if inventory[i] == 0 or not (x_remain >= 2**i and y_remain >= 2**i and z_remain >= 2**i):
            continue
        
        x_enable = x_remain // (2**i)
        y_enable = y_remain // (2**i)
        z_enable = z_remain // (2**i)
        
        used_blocks = min(inventory[i], x_enable * y_enable * z_enable)
        count += used_blocks
        inventory[i] -= used_blocks
        
        used_z = used_blocks // (x_enable * y_enable) * (2**i)
        used_y = ((used_blocks % (x_enable * y_enable)) // x_enable) * (2**i)
        used_x = ((used_blocks % (x_enable * y_enable)) % x_enable) * (2**i)
        
        remain_parts = []
        if x_remain - used_x > 0:
            remain_parts.append((x_remain - used_x, y_remain, z_remain))
        if y_remain - used_y > 0:
            remain_parts.append((used_x, y_remain - used_y, z_remain))
        if z_remain - used_z > 0:
            remain_parts.append((x_remain, y_remain, z_remain - used_z))
        
        for part in remain_parts:
            fill_box(part[0], part[1], part[2])
        return
    
    enable = False

fill_box(x, y, z)
if enable:
    print(count)
else:
    print(-1)