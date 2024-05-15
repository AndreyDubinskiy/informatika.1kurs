import pylab as p
from heapq import *


def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph


def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges()
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    # # print(V_num)
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1], edge[2])])
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

def Floyd_Warshall(graph):
    v = len(graph)
    d = [[ float('infinity') for i in range(v)]for j in range(v)]
    nxt = [[-1 for i in range(v)] for j in range(v)]
    for i in range(v):
        for j in range(v):
            if graph[i][j] != 0:
                d[i][j] = graph[i][j]
                nxt[i][j] = j
    for k in range(1, v):
        for i in range(v):
            for j in range(v):
                if d[i][k]+d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    nxt[i][j] = nxt[i][k]

    return d, nxt

def pth(i, j, nxt):
    # i = nxt[i][j]
    p = [i]
    while nxt[i-1][j-1] + 1 != j:
        i = nxt[i-1][j-1] + 1
        p.append(i)
    p.append(j)
    return p

graph = read_graph_as_neigh_list_w()
print(graph)