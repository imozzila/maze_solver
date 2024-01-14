from maze_solver.solver.nodes import Graph
from maze_solver.models.maze import Maze
from math import inf
import array as arr

"""def Dijkstra(maze: Maze, graph: Graph):
    dist = arr.array('i', [])
    for node in graph:
`"""

def DFS(maze: Maze, graph: Graph):
    stack = []
    visited_nodes = []
    """Depth First Search algorithm.
    Initial State: Entrance
    Goal State: Exit
    """
    stack.append(maze.entrance.index)
    
    while len(stack) != 0:
        print("Initial",stack)
        current_node = stack.pop()
        print("After",stack)
        if current_node == maze.exit.index:
            print("exit found")
            break
        visited_nodes.append(current_node)
        adjacent_nodes = graph.adjacency_list[current_node]
    
        known_nodes = set(visited_nodes).union(set(stack))
        not_visited = set(adjacent_nodes).difference(known_nodes)
        for i in not_visited:
            stack.append(i)

        
        
