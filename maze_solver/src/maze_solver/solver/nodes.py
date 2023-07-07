from maze_solver.models.maze import Maze
from dataclasses import dataclass 
from maze_solver.models.border import Border
from maze_solver.models.square import Square 
from collections import defaultdict

class Graph:
    def __init__(self, mazee:Maze):
        print('test')
        self.adjacency_list = defaultdict(list)
        self.mazee = mazee
        

    def add_edge(self, parent: int, child: int):
        self.adjacency_list[parent].append(child)

    def get_edges(self, node: int):
        return self.adjacency_list[node]
    

    def get_nodes(self):
        for square in self.mazee:
            if square.border & Border.RIGHT:
                pass
            else:
                node = self.mazee.squares[square.row * self.mazee.width + 1] #checks square to the right 
                self.add_edge(square.index, node.index)

            if square.border & Border.BOTTOM:
                pass
            else:
                node = self.mazee.squares[square.row + self.mazee.width + square.column] #checks square below
                self.add_edge(square.index, node.index)
            
def validate_nodes(node: Square):
    if Square.border & Border.RIGHT:
        pass
        