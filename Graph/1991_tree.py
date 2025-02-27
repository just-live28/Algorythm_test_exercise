# 전위순회, 중위순회, 후위순회 구현
# A - 65 -> 64를 빼면 1이됨.

n = int(input())
lc = [0] * (n+1)
rc = [0] * (n+1)
for _ in range(n):
    node, l, r = input().split()
    idx = ord(node) - 64
    if l != '.':
        lc[idx] = ord(l) - 64
    if r != '.':
        rc[idx] = ord(r) - 64

preorder_result = ''
def preorder(node):
    global preorder_result
    if node == 0:
        return
    preorder_result += chr(node+64)
    preorder(lc[node])
    preorder(rc[node])

inorder_result = ''
def inorder(node):
    global inorder_result
    if node == 0:
        return
    inorder(lc[node])
    inorder_result += chr(node+64)
    inorder(rc[node])

postorder_result = ''
def postorder(node):
    global postorder_result
    if node == 0:
        return
    postorder(lc[node])
    postorder(rc[node])
    postorder_result += chr(node+64)

preorder(1)
print(preorder_result)
inorder(1)
print(inorder_result)
postorder(1)
print(postorder_result)
