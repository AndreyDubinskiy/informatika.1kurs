def read_graph_as_edges():
    n = int(input())
    graph = [list(map(str, input().split())) for i in range(n)]
    return graph


def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges()
    graph_dict = {}  
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(int(edge[0]))
        vertex_set.add(int(edge[1]))
    V_num = len(vertex_set)
    # # print(V_num)
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        graph_dict[int(edge[0])] = graph_dict[int(edge[0])] | frozenset([(int(edge[1]), edge[2])])
    return graph_dict


def read_graph_as_neigh_matrix():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = edge[1]

    return res_matrix


def read_graph_as_neigh_matrix_w():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = edge[2]

    return res_matrix


def print_matrix(matrix):
    for line in matrix:
        print(*line)


def Dijkstra(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = '💩💩💩💩💩'

    d[v] = ''
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                print(neigh)
                if d[neigh[0]] == '💩💩💩💩💩':
                    if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                        d[neigh[0]] = d[c[1]] + neigh[1]
                    visited.append(neigh[::-1])
                else:
                    if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                        d[neigh[0]] = d[c[1]] + (neigh[1])
                    visited.append(neigh[::-1])

    return d


graph = read_graph_as_neigh_list_w()
b = Dijkstra(graph, 1)
print(graph)
print(b)