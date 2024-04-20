'''
This module contains 8 functions that work with graphs
'''

def get_graph_from_file(file_name: str)-> list[list[int]]:
    '''
    Read graph from file and return a list of edges.
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    '''
    with open(file_name, 'r', encoding = 'utf-8') as file:
        lst = file.readlines()
        for obj in enumerate(lst):
            ind,line = obj
            lst[ind] = [int(point) for point in line.strip().split(',')]
        return lst

def to_edge_dict(edge_list: list[list[int]])-> dict[int, int]:
    '''
    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    '''
    result = {}
    for pair in edge_list:
        for obj in enumerate(pair):
            ind, digit = obj
            if not digit in result:
                result[digit] = []
            if pair[ind-1] not in result[digit]:
                result[digit].append(pair[ind-1])
                result[digit].sort()
    return result

def is_edge_in_graph(graph: dict[int, int], edge: tuple[int, int])-> bool:
    '''
    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    '''
    return (edge[0] in graph) and (edge[1] in graph[edge[0]])

def add_edge(graph: dict[int, int], edge: tuple[int, int])-> dict[int, int]:
    """ 
    Add a new edge to the graph and return new graph. 
    
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if len(edge) == 2:
        for obj in enumerate(edge):
            ind, digit = obj
            if not digit in graph:
                graph[digit] = []
            graph[digit].append(edge[ind-1])
    else:
        graph[edge[0]] = []
    return graph

def del_edge(graph: dict[int, int], edge: tuple[int, int])-> dict[int, int]:
    """
    Delete an edge from the graph and return a new graph.
    
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    for obj in enumerate(edge):
        ind, digit = obj
        if digit in graph:
            if edge[ind-1] in graph[digit]:
                graph[digit].remove(edge[ind-1])
            elif graph[digit] == []:
                graph.pop(digit)
    return graph

def add_node(graph: dict[int, int], node: int)-> dict[int, int]:
    """ 
    Add a new node to the graph and return a new graph.
    
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if not node in graph:
        graph[node] = []
    return graph

def del_node(graph: dict[int, int], node: int)-> dict[int, int]:
    """ 
    Delete a node and all incident edges from the graph.
    
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    graph.pop(node, None)
    for key in graph:
        if node in graph[key]:
            graph[key].remove(node)
    return graph

def convert_to_dot(filename: str)-> None:
    """
    Get graph from a file and save the directed graph to a file in a DOT format with the same name.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete = False) as tmpfile:
    ...     _ = tmpfile.write('1,2\\n3,4\\n1,5')
    >>> convert_to_dot(tmpfile.name)
    >>> with open(tmpfile.name, 'r', encoding ='utf-8') as the_file:
    ...     print(the_file.readlines())
    ['digraph {\\n', '1 -> 2\\n', '1 -> 5\\n', '2 -> 1\\n', '3 -> 4\\n', \
'4 -> 3\\n', '5 -> 1\\n', '}']
    """
    lines = get_graph_from_file(filename)
    for line in lines:
        if line[0] != line[1] and not [line[1], line[0]] in lines:
            lines.append([line[1], line[0]])
    lines.sort(key = lambda a : a[0])
    with open(filename.replace('.txt','.dot'), 'w', encoding = 'utf-8') as file:
        file.write('digraph {\n')
        for line in lines:
            file.write(f'{str(line[0])} -> {str(line[1])}\n')
        file.write('}')

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
