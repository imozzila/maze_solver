from maze_solver.models.maze import Maze
from dataclasses import dataclass 
from maze_solver.models.border import Border
from maze_solver.models.square import Square 
from collections import defaultdict

class Graph:
    def __init__(self, maze:Maze):
        self.adjacency_list = defaultdict(list)
        self.maze = maze
        self.get_nodes()        

    def add_edge(self, parent: int, child: int):
        self.adjacency_list[parent].append(child)

    def get_edges(self, node: int):
        return self.adjacency_list[node]
    

    def get_nodes(self):
        for square in self.maze:
            if square.border & Border.RIGHT or square.column + 1 == self.maze.width:
                pass
            else:
                node = self.maze.squares[square.index + 1] #checks square to the right 
                self.add_edge(square.index, node.index)
                self.add_edge(node.index, square.index)

            if square.border & Border.BOTTOM or square.row + 1 == self.maze.height:
                pass
            else:
                node = self.maze.squares[square.index + self.maze.width] #checks square below
                self.add_edge(square.index, node.index)
                self.add_edge(node.index, square.index)


def validate_nodes(node: Square):
    if Square.border & Border.RIGHT:
        pass
        