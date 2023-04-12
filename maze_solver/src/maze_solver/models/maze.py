from dataclasses import dataclass
from functools import cached_property
from typing import Iterator

from maze_solver.models.square import Square

@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...]

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    def __getitem__(self, index: int) -> Square:
        return self.squares[index]

    @cached_property
    def width(self):
        return max(square.column for square in self) + 1
    
    @cached_property
    def height(self):
        return max(square.row for square in self) + 1
    