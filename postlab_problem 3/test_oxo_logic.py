import unittest
from oxo_logic import Game

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_new_game_board_empty(self):
        self.assertEqual(self.game.new_game(), [" "] * 9)

    def test_user_move_valid(self):
        self.game.new_game()
        result = self.game.user_move(0)
        self.assertEqual(self.game.board[0], "X")
        self.assertEqual(result, "")

    def test_user_move_invalid(self):
        self.game.new_game()
        self.game.board[0] = "X"
        with self.assertRaises(ValueError):
            self.game.user_move(0)

    def test_computer_move(self):
        self.game.new_game()
        result = self.game.computer_move()
        self.assertIn(result, ["", "O", "D"])

    def test_winning_condition(self):
        self.game.board = ["X", "X", " ", "O", "O", " ", " ", " ", " "]
        self.game.user_move(2)
        self.assertTrue(self.game._is_winning_move())

if __name__ == "__main__":
    unittest.main()

