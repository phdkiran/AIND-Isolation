"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer(search_depth=1)
        self.player2 = sample_players.GreedyPlayer()
        # self.game = isolation.Board(self.player1, self.player2, 8, 8)
        self.game = isolation.Board(self.player1, self.player2)

    def test_minimax(self):
        # print(dir(self.game), self.player1)
        # print(self.game.print_board())
        self.game.apply_move((1, 0))
        # print(self.game.print_board())
        # self.player1.get_move(self.game, 100)
        self.game.play()
        print(self.game.to_string())

        # print(self.game.get_legal_moves())

    def test_minimax_open_move(self):
        self.game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
                                  0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 56, 51]
        # print(self.game.print_board())
        self.game.play()
        print(self.game.print_board())


if __name__ == '__main__':
    unittest.main()
