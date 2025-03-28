import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# node = [num, left_child, right_child] ->[num, None, None]
nodes = []
while True:
    line = input()
    if line == '':
        break
    else:
        nodes.append(int(line))
    
def print_postorder(nodes):
    if not nodes:
        return
    root = nodes[0]
    idx = 1
    while idx < len(nodes) and nodes[idx] < root:
        idx += 1    
    print_postorder(nodes[1:idx])
    print_postorder(nodes[idx:])
    print(root)

print_postorder(nodes)