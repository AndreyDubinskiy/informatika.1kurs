from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)

def dfs(graph, node, visited, on_stack):
    visited[node] = True
    on_stack[node] = True
    for neighbor in graph.get(node, []):
        if not visited[neighbor]:
            if dfs(graph, neighbor, visited, on_stack):
                return True
        elif on_stack[neighbor]:
            return True
    on_stack[node] = False
    return False

def build_graph(arr, constraints):
    graph = defaultdict(list)

    for constraint in constraints:
        total = sum(val if i % 2 == 0 else -val for i, val in enumerate(constraint[:-1]))
        if total < 0:
            graph[-constraint[-1]].append(total - 1)
        else:
            graph[constraint[-1]].append(total + 1)

    return graph

def compatible_constraints(arr, constraints):
    graph = build_graph(arr, constraints)
    visited = {node: False for node in graph}
    on_stack = {node: False for node in graph}

    for node in graph:
        if not visited[node]:
            if dfs(graph, node, visited, on_stack):
                return False

    return True

arr = [1, 2, 3]
constraints = [(1, 3, 5), (-2, 2, 3)]
print(compatible_constraints(arr, constraints))