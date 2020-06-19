from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.setup_max_row_col()
        if self.max_col < 0 or self.max_row < 0:
            return

        visited = set()
        for row, row_list in enumerate(self.board):
            for col, symbol in enumerate(row_list):
                coords = (row, col)
                if symbol is 'O' and coords not in visited:
                    edge_group, o_set = self.o_group(coords)
                    if not edge_group:
                        self.make_all_X(o_set)
                    else:
                        visited |= o_set

    def o_group(self, start_coords):
        """
        Returns:
            (the group hits an edge, group) pair
        """
        if self.symbol(start_coords) is not 'O':
            return (False, set()) 
        cd_stack = [start_coords]
        visited = set(cd_stack)
        touches_edge = False

        while cd_stack:
            row, col = cd_stack.pop()
            touches_edge = touches_edge or self.on_edge(row, col)
            next_coords = [
                nb for nb in self.neighbours(row, col)
                if self.symbol(nb) is 'O' and nb not in visited
            ]
            cd_stack.extend(next_coords)
            for coord in next_coords:
                visited.add(coord)
        
        return (touches_edge, visited)

    def symbol(self, coords):
        return self.board[coords[0]][coords[1]]

    def setup_max_row_col(self):
        """
        Max row = the maximum number of places you can go down from 0
        Max col = the maximum number of places you can go accross from 0
        """
        self.max_row = len(self.board) - 1
        if self.max_row < 0:
            self.max_col = -1
        else:
            self.max_col = len(self.board[0]) - 1

    def on_edge(self, row, col):
        return row == 0 or col == 0 or row == self.max_row or col == self.max_col

    def neighbours(self, row, col):
        nb = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
        return [
            (r, c)
            for r, c in nb
            if 0 <= r <= self.max_row and 0 <= c <= self.max_col
        ]

    def make_all_X(self, o_set):
        for coord in o_set:
            row = coord[0]
            col = coord[1]
            self.board[row][col] = 'X'


def print_board(board):
    for row in board:
        print(row)

# board = [
#     ['X', 'X', 'X', 'X'],
#     ['X', 'O', 'O', 'X'],
#     ['X', 'X', 'O', 'X'],
#     ['X', 'O', 'X', 'X']
# ]

board = [
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['X', 'X', 'X', 'X', 'X', 'O'],
    ['O', 'O', 'X', 'O', 'X', 'O'],
    ['X', 'X', 'X', 'X', 'X', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O']
]

Solution().solve(board)

print_board(board)



# The faster solution goes from the outside, finds Os (and their inside O neighbours), changes them into Ns,
#   then changes all remaining Os to Xs and all Ns back to Os