"""
Solution for LeetCode 994: Rotting Oranges
This problem is a perfect example of a multi-source, layered Breadth-First Search.
"""
from collections import deque
from typing import List

def rottingOrange(grid: List[List[int]]) -> int:
  if not grid:
    return 0

  n_rows, n_cols = len(grid), len(grid[0])
  fresh_oranges = 0
  q = deque()
  for r in range(n_rows):
    for c in range(n_cols):
      value = grid[r][c]
      if value == 1:
        fresh_oranges += 1
      if value == 2:
        q.appendleft((r, c))

  minutes_elapsed = 0
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  
  while q and fresh_oranges > 0:
    layer_size = len(q)
    for _ in range(layer_size):
      r, c = q.pop()
      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] == 1:
          grid[nr][nc] = 2
          fresh_oranges -= 1
          q.appendleft((nr, nc))
    minutes_elapsed += 1

return minutes_elapsed if fresh_oranges > 0 else -1
