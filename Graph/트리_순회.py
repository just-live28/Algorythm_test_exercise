n = int(input())

nodes = {}
for _ in range(n):
    node, lc, rc = input().split()
    nodes[node] = (lc, rc)

preorder_result = []
def preorder(node):
    preorder_result.append(node)
    left_child, right_child = nodes[node][0], nodes[node][1]
    if left_child != '.':
        preorder(left_child)
    if right_child != '.':
        preorder(right_child)

inorder_result = []
def inorder(node):
    left_child, right_child = nodes[node][0], nodes[node][1]
    if left_child != '.':
        inorder(left_child)
    inorder_result.append(node)
    if right_child != '.':
        inorder(right_child)

postorder_result = []
def postorder(node):
    left_child, right_child = nodes[node][0], nodes[node][1]
    if left_child != '.':
        postorder(left_child)
    if right_child != '.':
        postorder(right_child)
    postorder_result.append(node)    
    
preorder('A')
inorder('A')
postorder('A')
print(''.join(preorder_result))
print(''.join(inorder_result))
print(''.join(postorder_result))