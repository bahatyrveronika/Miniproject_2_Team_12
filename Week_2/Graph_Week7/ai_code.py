'''
This module contains 8 functions that work with graphs
'''

from collections import defaultdict

def get_graph_from_file(file_name: str)-> list[list[int]]:
    '''
    Read graph from file and return a list of edges.
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    '''
    with open(file_name, 'r', encoding = 'utf-8') as file:
        return [list(map(int, line.strip().split(','))) for line in file.readlines()]

def to_edge_dict(edge_list: list[list[int]])-> dict[int, list[int]]:
    '''
    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    '''
    result = defaultdict(list)
    for edge in edge_list:
        for vertex in edge:
            result[vertex].append(edge[0] if vertex != edge[0] else edge[1])
    return {key: sorted(value) for key, value in result.items()}

def is_edge_in_graph(graph: dict[int, list[int]], edge: tuple[int, int])-> bool:
    '''
    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 2))
    True
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    False
    '''
    return edge[0] in graph and edge[1] in graph[edge[0]]

def add_edge(graph: dict[int, list[int]], edge: tuple[int, int])-> dict[int, list[int]]:
    '''
    Add a new edge to the graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    '''
    for vertex in edge:
        other = edge[0] if vertex != edge[0] else edge[1]
        if vertex not in graph:
            graph[vertex] = []
        graph[vertex].append(other)
    return graph

def del_edge(graph: dict[int, list[int]], edge: tuple[int, int])-> dict[int, list[int]]:
    '''
    Remove an edge from the graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    '''
    if edge[0] in graph and edge[1] in graph[edge[0]]:
        graph[edge[0]].remove(edge[1])
    if edge[1] in graph and edge[0] in graph[edge[1]]:
        graph[edge[1]].remove(edge[0])

    return graph

def add_node(graph: dict[int, list[int]], node: int)-> dict[int, list[int]]:
    '''
    Add a new node to the graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    '''
    graph.setdefault(node, [])
    return graph

def del_node(graph: dict[int, list[int]], node: int)-> dict[int, list[int]]:
    '''
    Remove a node from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    '''
    for edge in list(graph.keys()):
        if node in graph[edge]:
            graph[edge].remove(node)
    graph.pop(node, None)
    return graph

def convert_to_dot(filename: str)-> None:
    '''
    Convert a graph from text file to dot format.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete = False) as tmpfile:
    ...     _ = tmpfile.write('1,2\\n3,4\\n1,5')
    >>> convert_to_dot(tmpfile.name)
    >>> with open(tmpfile.name, 'r', encoding ='utf-8') as the_file:
    ...     print(the_file.readlines())
    ['digraph {\\n', '1 -> 2\\n', '1 -> 5\\n', '2 -> 1\\n', '3 -> 4\\n', \
'4 -> 3\\n', '5 -> 1\\n', '}']
    '''
    lines = get_graph_from_file(filename)
    edges = set()
    for line in lines:
        u, v = line
        edges.add((u, v))
        edges.add((v, u))
    with open(filename.replace('.txt','.dot'), 'w', encoding = 'utf-8') as file:
        file.write('digraph {\n')
        for edge in sorted(edges):
            file.write(f'{edge[0]} -> {edge[1]}\n')
        file.write('}')

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
