n = int(input())
graph = {}
for i in range(1, n+1):
    a, b, c = input().split()
    graph[a] = [b, c]

preorder_result = []
def preorder_travel(now, result):
    result.append(now)
    
    a, b = graph[now]
    if a != '.':
        preorder_travel(a, result)
    if b != '.':
        preorder_travel(b, result)

inorder_result = []
def inorder_travel(now, result):
    a, b = graph[now]
    
    if a != '.':
        inorder_travel(a, result)
    result.append(now)
    if b != '.':
        inorder_travel(b, result)

postorder_result = []
def postorder_travel(now, result):
    a, b = graph[now]

    if a != '.':
        postorder_travel(a, result)
    if b != '.':
        postorder_travel(b, result)
    result.append(now)

preorder_travel('A', preorder_result)
inorder_travel('A', inorder_result)
postorder_travel('A', postorder_result)

print(''.join(preorder_result))
print(''.join(inorder_result))
print(''.join(postorder_result))