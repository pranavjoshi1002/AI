graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited_bfs = []
visited_dfs = set()
queue = []


def bfs(visited, g, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in g[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def dfs(visited, g, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in g[node]:
            dfs(visited, g, neighbour)


print("Following is the Breadth-First Search : ")
bfs(visited_bfs, graph, '5')
print(" ")
print("Following is Depth-First Search : ")
dfs(visited_dfs, graph, '5')
