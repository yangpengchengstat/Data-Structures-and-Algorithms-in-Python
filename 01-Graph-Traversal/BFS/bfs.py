"""
Python implementation of Breadth-First Search (BFS) and related pathfinding algorithms.
Based on MIT 6.006 course materials.
"""

def bfs(adj, s):
    """
    Performs Breadth-First Search on a graph to find shortest paths from a source.

    Args:
        adj (list of lists): An adjacency list representation of the graph.
                             adj[i] contains a list of neighbors of vertex i.
        s (int): The source vertex to start the search from.

    Returns:
        list: A parent array where parent[v] is the vertex that discovered v.
              This array represents the shortest-path tree.
              parent[s] is s, and parent[v] is None if v is not reachable from s.
    """
    # O(V) to initialize the parent array. Can use a hash map if vertices are not 0-indexed.
    parent = [None for _ in adj]
    parent[s] = s  # The root of the BFS tree is the source itself

    # O(1) to initialize levels. level[i] will store all vertices at distance i from s.
    level = [[s]]

    # The loop continues as long as the last level we discovered is not empty.
    while len(level[-1]) > 0:
        level.append([])  # Create a new, empty level for the next layer of vertices

        # For each vertex u in the last fully discovered level...
        for u in level[-2]:
            # ...explore its neighbors.
            for v in adj[u]:
                # If the neighbor v has not been visited yet (parent is None)...
                if parent[v] is None:
                    parent[v] = u  # ...set its parent to u...
                    level[-1].append(v)  # ...and add it to the new level.
    
    return parent

def unweighted_shortest_path(adj, s, t):
    """
    Finds the shortest path in an unweighted graph from source s to target t.

    Args:
        adj (list of lists): The adjacency list of the graph.
        s (int): The source vertex.
        t (int): The target vertex.

    Returns:
        list: A list of vertices representing the shortest path from s to t.
              Returns None if t is not reachable from s.
    """
    # O(V + E) to run BFS and get the shortest-path tree.
    parent = bfs(adj, s)

    # O(1) to check if a path exists.
    if parent[t] is None:
        return None  # t is not reachable from s

    # O(V) in the worst case to reconstruct the path by backtracking.
    path = [t]
    curr = t
    while curr != s:
        curr = parent[curr]
        path.append(curr)
    
    # The path is constructed backwards, so we reverse it before returning.
    return path[::-1]

if __name__ == '__main__':
    # Example Graph G1 from the recitation notes (directed)
    # V = {0, 1, 2, 3, 4}
    # E = {(0,1), (1,2), (2,0), (3,4)}
    adj1 = [
        [1],       # Neighbors of 0
        [2],       # Neighbors of 1
        [0],       # Neighbors of 2
        [4],       # Neighbors of 3
        []         # Neighbors of 4
    ]

    print("--- Example 1: Directed Graph G1 ---")
    parent_tree_g1 = bfs(adj1, 0)
    print(f"Parent array starting from 0: {parent_tree_g1}") # Expected: [0, 0, 1, None, None]
    path_0_to_2 = unweighted_shortest_path(adj1, 0, 2)
    print(f"Shortest path from 0 to 2: {path_0_to_2}") # Expected: [0, 1, 2]
    path_0_to_3 = unweighted_shortest_path(adj1, 0, 3)
    print(f"Shortest path from 0 to 3: {path_0_to_3}") # Expected: None

    print("\n" + "="*40 + "\n")

    # Example Graph G2 from the recitation notes (undirected)
    # V = {0, 1, 2, 3, 4}
    # E = {{0,1}, {0,3}, {0,4}, {2,3}}
    adj2 = [
        [1, 3, 4], # Neighbors of 0
        [0],       # Neighbors of 1
        [3],       # Neighbors of 2
        [0, 2],    # Neighbors of 3
        [0]        # Neighbors of 4
    ]
    
    print("--- Example 2: Undirected Graph G2 ---")
    parent_tree_g2 = bfs(adj2, 0)
    print(f"Parent array starting from 0: {parent_tree_g2}") # Expected: [0, 0, 3, 0, 0]
    path_0_to_2 = unweighted_shortest_path(adj2, 0, 2)
    print(f"Shortest path from 0 to 2: {path_0_to_2}") # Expected: [0, 3, 2]

