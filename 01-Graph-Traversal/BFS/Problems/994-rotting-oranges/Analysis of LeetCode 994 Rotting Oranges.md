### Analysis of LeetCode 994: Rotting Oranges

This problem is a classic example of a graph traversal problem that is perfectly suited for a **Multi-Source Breadth-First Search (BFS)**. The key is to recognize that the grid itself can be modeled as a graph, and the rotting process is equivalent to exploring this graph layer by layer.

---

### 1. Modeling the Problem as a Graph

First, let's re-frame the problem in graph theory terms:

* **Vertices (Nodes)**: Each cell `(row, col)` in the grid can be considered a vertex in our graph.
* **Edges**: An edge exists between two vertices (cells) if they are 4-directionally adjacent. Since the rotting can spread in any of the four directions, the graph is **unweighted** and **undirected**.
* **Traversal**: The process of oranges rotting over time is a graph traversal. The rotting spreads from rotten oranges to their fresh neighbors, which is identical to how a search algorithm explores from a node to its adjacent nodes.

---

### 2. Why Breadth-First Search (BFS) is the Right Choice

Several clues in the problem statement point directly to BFS:

* **Shortest Path / Minimum Time**: The problem asks for the "minimum number of minutes." In an unweighted graph, BFS is guaranteed to find the shortest path from a source to all other nodes. Here, "path length" is equivalent to "minutes elapsed."
* **Simultaneous Process**: The rotting happens simultaneously from all rotten oranges. This means the process expands outwards in layers from all sources at the same time. This is a perfect fit for a **multi-source BFS**, where we initialize the search queue with all starting rotten oranges.
* **Layer-by-Layer Exploration**: The concept of "every minute" directly corresponds to processing one "level" or "layer" in a BFS traversal. All oranges at distance `k` from the nearest initial rotten orange will rot at minute `k`.

---

### 3. Algorithm Outline

A layered, multi-source BFS provides an elegant solution:

1.  **Initialization**:
    * Create a queue (e.g., a `deque` in Python) to store the coordinates of rotten oranges.
    * Iterate through the entire grid once to:
        * Find all initially rotten oranges (value `2`) and add their `(row, col)` coordinates to the queue.
        * Count the total number of fresh oranges (value `1`). This count is crucial for the final check.
2.  **Edge Case Check**: If there are no fresh oranges to begin with, the process takes 0 minutes. Return `0` immediately.
3.  **Layered BFS Traversal**:
    * Keep a counter for `minutes_elapsed`, initialized to 0.
    * Start a `while` loop that continues as long as the queue is not empty and there are still fresh oranges left.
    * Inside the loop, we process one "minute" (one layer):
        * First, get the current size of the queue. This represents all the oranges that became rotten in the previous minute.
        * Loop that many times, dequeuing one rotten orange at a time.
        * For each rotten orange, check its four neighbors (up, down, left, right).
        * If a neighbor is a valid grid cell and contains a fresh orange (value `1`):
            * Mark the orange as rotten by changing its value to `2`.
            * Add the neighbor's coordinates to the queue to be processed in the *next* minute.
            * Decrement the `fresh_oranges` counter.
        * After the inner loop finishes (processing one full layer), increment `minutes_elapsed`.
4.  **Final Result**:
    * After the `while` loop terminates, check the `fresh_oranges` counter.
    * If `fresh_oranges` is `0`, it means all oranges were successfully rotted. Return `minutes_elapsed`.
    * If `fresh_oranges` is greater than `0`, it means some fresh oranges were isolated and could not be reached. In this case, return `-1`.

---

### 4. Complexity Analysis

* **Time Complexity: `O(m * n)`**
    * Each cell in the `m x n` grid is visited at most once during the initial scan and at most once during the BFS traversal. Therefore, the time complexity is linear in the number of cells.
* **Space Complexity: `O(m * n)`**
    * In the worst-case scenario (e.g., a checkerboard pattern of oranges), the queue could hold up to half of the cells. Therefore, the space required is also proportional to the number of cells in the grid.
