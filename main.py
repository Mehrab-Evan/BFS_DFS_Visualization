import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


# Function to perform BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    stages = [list(queue)]

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
            stages.append(list(queue))

    return visited, stages


def dfs(graph, start):
    visited = set()
    stack = [start]
    stages = [list(stack)]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
            stages.append(list(stack))

    return visited, stages


st.title("DFS and BFS Visualization")

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

G = nx.Graph(graph)

algorithm = st.sidebar.selectbox("Select Algorithm", ("BFS", "DFS"))

start_node = st.sidebar.selectbox("Select Starting Node", list(graph.keys()))

if algorithm == "BFS":
    visited, stages = bfs(graph, start_node)
else:
    visited, stages = dfs(graph, start_node)

st.subheader("Graph Visualization")
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=20, font_weight='bold',
        edge_color='gray')
st.pyplot(plt.gcf())
plt.clf()


st.subheader(f"{algorithm} Stages")
for i, stage in enumerate(stages):
    st.write(f"Stage {i + 1}: {stage}")
