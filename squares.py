#!/usr/bin/env python
import os
from enum import Enum

class Color(Enum):
    blue = 0
    grey = 1
    red = 2

class Direction(Enum):
    left = 0
    right = 1
    top = 2
    bottom = 3

class Square:

    def __init__(self, color, direction, x, y):
        self.x = x
        self.y = y
        self.direction = direction
        self.color = color

    def move(self, direction=None):
        if direction is None:
            direction = self.direction
        if direction == Direction.left:
            self.y -= 1
        if direction == Direction.right:
            self.y += 1
        if direction == Direction.top:
            self.x -= 1
        if direction == Direction.bottom:
            self.x += 1

    def bounds(self, length, width):
        if self.x > length or\
                self.x < 0 or\
                self.y > width or\
                self.y < 0:
            raise IndexError()

class BoardSquare:

    def __init__(self, color=None, direction=None):
        self.color=color
        self.direction = direction

    def isDumb(self):
        if self.color is None and self.direction is None:
            return True
        else:
            return False

    def __str__(self):
        if self.isDumb():
            return "."

        elif self.color is not None:
            if self.color == Color.blue:
                return '\033[94mo\033[0m'
            if self.color == Color.grey:
                return '\033[92mo\033[0m'
            if self.color == Color.red:
                return '\033[91mo\033[0m'

        elif self.direction is not None:
            if self.direction == Direction.left:
                return '<'
            elif self.direction == Direction.right:
                return '>'
            elif self.direction == Direction.top:
                return '^'
            elif self.direction == Direction.bottom:
                return '!'


class Board:

    def __init__(self, x, y):
        self.squares = [[BoardSquare() for i in range(x)] for j in range(y)]
        self.length = x-1
        self.width = y-1

    def setColor(self, x, y, color):
        self.squares[x][y].color = color

    def setDirection(self, x, y, direction):
        self.squares[x][y].direction = direction

    def __str__(self):
        return os.linesep.join([" ".join(map(str, line)) for line in self.squares])

class Game:

    def __init__(self):
        self.board = Board(10, 10)
        self.squares = []

    def addSquare(self, square):
        self.squares.append(square)

    def findSquare(self, color):
        for square in self.squares:
            if square.color == color:
                return square
        raise StopIteration

    def moveSquare(self, color, direction=None):
        square = self.findSquare(color)
        square.move(direction)
        square.bounds(self.board.length, self.board.width)
        cur_pos = self.board.squares[square.x][square.y]
        if not cur_pos.isDumb():
            if cur_pos.direction is not None:
                square.direction = cur_pos.direction

        for sq in [s for s in self.squares if not s == square]:
            if sq.x == square.x and sq.y == square.y:
                self.moveSquare(sq.color, square.direction)


    def isDone(self):
        try:
            under_colors = [self.board.squares[sq.x][sq.y].color for sq in self.squares]
        except IndexError:
            raise IndexError(str([(sq.color, sq.x, sq.y) for sq in self.squares]))

        sq_colors = [sq.color for sq in self.squares]
        done = [u == s for u, s in zip(under_colors, sq_colors)]
        return all(done)
