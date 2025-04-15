from Mancala import Mancala
import unittest


class Tests(unittest.TestCase):

    def test_get_valid_moves(self):
        game = Mancala(pits_per_player=6, stones_per_pit=4)

        expected_moves = [1, 2, 3, 4, 5, 6]
        self.assertEqual(game.get_valid_moves(), expected_moves)


if __name__ == '__main__':
    unittest.main()


