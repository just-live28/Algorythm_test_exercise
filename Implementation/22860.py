import sys
input = sys.stdin.readline

def traverse_fs(target, types):
    global count
    if target not in fs:
        return
    
    for name, is_dir in fs[target]:
        if not is_dir:
            if name not in types:
                types.add(name)
            count += 1
        else:
            traverse_fs(name, types)
    
fs = {}
n, m = map(int, input().split())
for _ in range(n+m):
    parent, name, val = input().rstrip().split()
    
    fs.setdefault(parent, [])
    fs[parent].append([name, int(val)])

q = int(input())
for _ in range(q):
    line = input().rstrip().split('/')
    types = set()
    count = 0
    traverse_fs(line[-1], types)
    
    print(len(types), count)