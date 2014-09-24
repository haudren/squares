import unittest
from squares import *
from simulator import Simulator

class move(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_up(self):
        self.game.addSquare(Square(Color.red, Direction.top, 0, 0))
        self.assertRaises(IndexError, self.game.moveSquare, Color.red)

    def test_up_2(self):
        self.game.addSquare(Square(Color.red, Direction.top, 0, 0))
        self.game.addSquare(Square(Color.blue, Direction.top, 0, 1))
        self.game.addSquare(Square(Color.grey, Direction.top, 0, 2))
        self.assertRaises(IndexError, self.game.moveSquare, Color.grey)

    def test_down(self):
        self.game.addSquare(Square(Color.red, Direction.bottom, 10, 10))
        self.assertRaises(IndexError, self.game.moveSquare, Color.red)

    def test_right(self):
        self.game.addSquare(Square(Color.red, Direction.right, 10, 10))
        self.assertRaises(IndexError, self.game.moveSquare, Color.red)

    def test_left(self):
        self.game.addSquare(Square(Color.red, Direction.left, 0, 0))
        self.assertRaises(IndexError, self.game.moveSquare, Color.red)

class level_0(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.addSquare(Square(Color.red, Direction.bottom, 0, 0))
        self.game.board.setColor(2, 0, Color.red)

        self.simulator = Simulator(self.game)

    def test_goal(self):
        self.game.moveSquare(Color.red)
        self.game.moveSquare(Color.red)
        self.assertTrue(self.game.isDone())

    def test_simulation(self):
        print self.simulator.find_solution()

class level_1(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.addSquare(Square(Color.blue, Direction.bottom, 0, 0))
        self.game.board.setColor(1, 0, Color.blue)
        self.game.addSquare(Square(Color.red, Direction.top, 3, 0))
        self.game.board.setColor(2, 0, Color.red)

        self.simulator = Simulator(self.game)

    def test_goal(self):
        self.game.moveSquare(Color.red)
        self.game.moveSquare(Color.blue)
        self.assertTrue(self.game.isDone())

    def test_simulation(self):
        print self.simulator.find_solution()

class level_2(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.addSquare(Square(Color.blue, Direction.top, 2, 1))
        self.game.board.setColor(0, 1, Color.blue)
        self.game.addSquare(Square(Color.red, Direction.right, 0, 0))
        self.game.board.setColor(0, 2, Color.red)
        self.game.addSquare(Square(Color.grey, Direction.left, 1, 3))
        self.game.board.setColor(1, 1, Color.grey)

        self.simulator = Simulator(self.game)

    def test_goal(self):
        self.game.moveSquare(Color.red)
        self.assertTrue(not self.game.isDone())
        self.game.moveSquare(Color.red)
        self.assertTrue(not self.game.isDone())
        self.game.moveSquare(Color.blue)
        self.assertTrue(not self.game.isDone())
        self.game.moveSquare(Color.blue)
        self.assertTrue(not self.game.isDone())
        self.game.moveSquare(Color.grey)
        self.assertTrue(not self.game.isDone())
        self.game.moveSquare(Color.grey)
        self.assertTrue(self.game.isDone())

    def test_simulation(self):
        print self.simulator.find_solution()

class level_31(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.addSquare(Square(Color.blue, Direction.bottom, 0, 2))
        self.game.board.setColor(2, 0, Color.blue)
        self.game.addSquare(Square(Color.red, Direction.left, 2, 3))
        self.game.board.setColor(2, 2, Color.red)
        self.game.addSquare(Square(Color.grey, Direction.right, 1, 1))
        self.game.board.setColor(2, 4, Color.grey)

        self.game.board.setDirection(1, 1, Direction.right)
        self.game.board.setDirection(0, 2, Direction.bottom)
        self.game.board.setDirection(2, 3, Direction.left)
        self.game.board.setDirection(4, 2, Direction.top)

        self.simulator = Simulator(self.game)

    def test_simulation(self):
        print
        print self.game.board
        print self.simulator.find_solution()

if __name__ == '__main__':
    unittest.main()
