# Assignment 4: Bellman-Ford Distance Vector Routing

## Overview

This project implements the Bellman-Ford algorithm for computing shortest paths in a directed graph. Each node calculates the minimum distance to every other node using an adjacency matrix representation of the graph. The algorithm supports negative edge weights, infinity values, and negative cycle detection.

## Objectives

- Implement the Bellman-Ford algorithm from each node's perspective.
- Handle packet loss, infinite paths, and negative cycles.
- Format and display results according to assignment specifications.
- Convert 1D matrix input into 2D adjacency matrix format.

## Problem Description

- Input: A square N x N adjacency matrix representing a graph.
- Output: For each node, print the shortest distance array from that node to all other nodes.
- If a node cannot reach another node, the distance is reported as inf.
- If a node is part of a negative cycle, the entire distance array for that node is None.

## Standard Input

- First line: An integer N (1 ≤ N ≤ 50), the number of nodes.
- Next N*N lines: Each line represents a matrix entry:
  - Integer (positive/negative): weight of the edge.
  - 'f': no edge (interpreted as infinity).

## Standard Output

- One line per node:
  ```
  Node i: distance_array
  ```
  Example:
  ```
  Node 0: [0, 5, inf, 7]
  ```

## Code Highlights

- `get_input()`: Reads N and the matrix values from input.
- `make_2d_matrix(size, matrix)`: Converts flat matrix into 2D list.
- `find_shortest_paths(size, graph)`: Applies Bellman-Ford from each node.
- Negative cycle detection results in all distances being set to None.

## How to Run

```bash
python distance_vector.py
```

Provide input interactively or via input redirection.

## Example Input

```
3
0
1
f
f
0
-1
1
f
0
```

## Example Output

```
Node 0: [0, 1, None]
Node 1: [None, None, None]
Node 2: [None, None, None]
```

## Notes

- The implementation handles up to 50 nodes efficiently.
- Infinite distance is represented as float('inf').
- Be cautious about integer overflows and floating-point precision in actual deployments.

## License

This project is part of CS 3357A - Computer Networks I at Western University. For academic use only.
