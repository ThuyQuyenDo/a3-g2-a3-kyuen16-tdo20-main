from a2d import Graph
from a3_parta import MinHeap

def minimum_spanning_tree(graph):
    mst = []
    visited = set()
    start_vertex = 0
    visited.add(start_vertex)
    edges = [
        (cost, start_vertex, to)
        for to, cost in graph.get_connected(start_vertex)
    ]
    heap = MinHeap(edges)

    while not heap.is_empty():
        cost, frm, to = heap.extract_min()
        if to not in visited:
            visited.add(to)
            mst.append((frm, to))
            for to_next, cost_next in graph.get_connected(to):
                if to_next not in visited:
                    heap.insert((cost_next, to, to_next))

    return mst