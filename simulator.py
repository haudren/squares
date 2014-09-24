from squares import *
from copy import deepcopy
import os

class Simulator:

    def __init__(self, game):
        self.init_game = game
        self.cur_game = deepcopy(game)
        self.tree = MoveTree(MoveNode(None, None, self.init_game.squares))

    def next(self, tree):
        leaves = []
        for color in [sq.color for sq in tree.node.squares]:
            self.cur_game.squares = deepcopy(tree.node.squares)
            try:
                self.cur_game.moveSquare(color)
            except IndexError:
                continue

            c_tree = MoveTree(MoveNode(tree, color, deepcopy(self.cur_game.squares)))
            tree.children.append(c_tree)
            leaves.append(c_tree)
            if self.cur_game.isDone():
                return True, leaves, c_tree

        return False, leaves, None

    def find_solution(self):
        success, leaves, final = self.next(self.tree)
        while not success:
            next_leaves = []
            for l in leaves:
                s, ls, f = self.next(l)
                next_leaves += ls

                if s:
                    print "Found it !"
                    success = s
                    final = f
                    break

            leaves = next_leaves

        return self.path(final)

    def path(self, tree):
        ancestors = [tree.node.color]
        ancestor = tree.node.parent
        while ancestor is not None:
            ancestors.append(ancestor.node.color)
            ancestor = ancestor.node.parent

        return ancestors

class MoveTree:
    def __init__(self, node):
        self.node = node
        self.children = []

    def walk(self):
        yield self.node
        for child in self.children:
            for n in child.walk():
                yield n

    def __str__(self):
        return str(self.node)+os.linesep+" ".join(map(str, self.children))

class MoveNode:
    def __init__(self, parent, color, squares):
        self.parent = parent
        self.color = color
        self.squares = squares

    def __str__(self):
        if self.color is not None:
            return str(self.color.value)
        else:
            return 'Root'
