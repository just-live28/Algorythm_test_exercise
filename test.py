from graphviz import Digraph

# 인접 행렬 (1~5번 노드 기준)
adj_matrix = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0]
]

dot = Digraph()

# 노드 추가 (1~5)
for i in range(1, 6):
    dot.node(str(i))

# 엣지 추가
for i in range(5):
    for j in range(5):
        if adj_matrix[i][j] == 1:
            dot.edge(str(i + 1), str(j + 1))

dot.render('graph_output', format='png', cleanup=True)
# dot.view()  # 주석 해제하면 이미지 바로 볼 수 있어요
