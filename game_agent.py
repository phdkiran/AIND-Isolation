"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves)
    # raise NotImplementedError


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - 2 * opp_moves)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    w, h = game.width / 2., game.height / 2.
    y, x = game.get_player_location(player)
    return float((h - y)**2 + (w - x)**2)


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax_ply(self, game, depth, init_move=None, min_max=None):
        """
        Helper function for minimax
        min_max : True for max function and False for min function
        Returns : (score and the position)
        """

        # depth is given as argument
        # while reached depth or leaf nodes reached, fill up all possible moves
        # get_legal_moves gives a list
        # Calculate the scores at the leaf or max depth
        # Apply min-max algorithm at each layer doing depth first
        # recursively call minimax function to achieve this

        # clever way to use max or min function
        min_max_func = max if min_max else min
        best_move = (-1, -1)
        beta_score = float('-inf')
        alpha_score = float('inf')
        # clever way to set value based on max or min function
        best_score = beta_score if min_max else alpha_score

        if self.time_left() < self.TIMER_THRESHOLD:
            print('timeout')
            raise SearchTimeout()

        if depth == 0:
            # reached the ply to calculate score
            calc_score = self.score(game, self)
            unit_score = min_max_func([best_score, calc_score])
            # print('leaf: score {} and move {} min_max: {}'.format( unit_score, init_move, min_max_func))
            return (unit_score, init_move)

        all_legal_moves = game.get_legal_moves()
        # print('total moves for {} at depth {} are {} and moves are {}'.format(init_move, depth, len(all_legal_moves), all_legal_moves))

        if not all_legal_moves:
            print('no moves')
            return (best_score, best_move)

        # while reached depth or leaf nodes reached, fill up all possible moves
        for each_move in all_legal_moves:
            # fore cast move
            tree_ply = game.forecast_move(each_move)
            # print(f'current move is {each_move}')
            # recurse
            (score, move) = self.minimax_ply(tree_ply,
                                             depth - 1, each_move, min_max=not min_max)
            # print('got tuple {} best score is {}', (score, move), best_score)
            # Check if the score is any better
            if score != best_score:
                best_score = min_max_func([score, best_score])
                if best_score == score:
                    # change move since it got the better score # fixed bug # was returning move
                    best_move = each_move
                    # print('depth {} changed to best move {} and best score {} move {}'.format(depth, best_move, best_score, each_move))
        pass  # for loop
        return (best_score, best_move)

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # call the helper function
        (score, move) = self.minimax_ply(
            game, depth, init_move=None, min_max=True)
        # print('score is {} and best move is {}'.format(score, move))
        return move


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!
        best_move = (-1, -1)
        # start with depth 1 and increment if time left
        # you will end up with best score top down plys
        depth = 1
        # print('ab test get move', self.time_left)
        try:
            # while self.time_left() > 0 and depth <= 25:
            while self.time_left() > 0:  # no depth limit
                # and depth <= self.search_depth:
                best_move = self.alphabeta(game, depth)
            # increment depth
            # print('increasing depth in ab test ', depth)
                depth += 1
        except SearchTimeout:
            # print('timed out at depth ', depth)
            # print('best_move is: ', best_move)
            pass
        return best_move

    def alphabeta_ply(self, game, depth, init_move=None, min_max=None, alpha_score=float('inf'), beta_score=float('-inf')):
        """
        Helper function for minimax
        min_max: True for max function and False for min function
        Returns: (score and the position)
        """

        # depth is given as argument
        # while reached depth or leaf nodes reached, fill up all possible moves
        # get_legal_moves gives a list
        # Calculate the scores at the leaf or max depth
        # Apply min-max algorithm at each layer doing depth first
        # recursively call minimax function to achieve this

        # clever way to use max or min function
        min_max_func = max if min_max else min
        best_move = (-1, -1)
        # clever way to set value based on max or min function
        best_score = beta_score if min_max else alpha_score

        if self.time_left() < self.TIMER_THRESHOLD:
            # print('timeout')
            raise SearchTimeout()

        if depth == 0:
            # reached the ply to calculate score
            calc_score = self.score(game, self)
            unit_score = min_max_func([best_score, calc_score])
            # print('leaf: score {} and move {} min_max: {}'.format( unit_score, init_move, min_max_func))
            return (unit_score, init_move)

        all_legal_moves = game.get_legal_moves()
        # print('total moves for {} at depth {} are {} and moves are {}'.format(init_move, depth, len(all_legal_moves), all_legal_moves))

        if not all_legal_moves:
            # print('no moves')
            return (best_score, best_move)

        # while reached depth or leaf nodes reached, fill up all possible moves
        for each_move in all_legal_moves:
            # fore cast move
            tree_ply = game.forecast_move(each_move)
            # print(f'current move is {each_move}')
            # print(f'best_score {best_score} and alpha {alpha_score} and beta {beta_score} max is {min_max}')
            # recurse
            (score, move) = self.alphabeta_ply(tree_ply,
                                               depth - 1, each_move, not min_max, alpha_score, beta_score)
            # print('got tuple {} best score is {} and function is {}'.format( (score, move), best_score, min_max_func))
            # Check if the score is any better
            if score != best_score:
                best_score = min_max_func([score, best_score])
                if best_score == score:
                    # change move since it got the better score # fixed bug # was returning move
                    best_move = each_move
                    # update alpha beta scores based on the min_max function
                    # print( f'move {move} score: {best_score} alpha: {alpha_score} beta: {beta_score} ')
                    if min_max:
                        # check for pruning
                        # Max node: score must be >= beta
                        if best_score >= beta_score:
                            # print( f'pruning max node score: {best_score} beta: {beta_score} ')
                            return (best_score, best_move)
                        alpha_score = max([best_score, alpha_score])
                    else:
                        # check for pruning
                        # Min node: score must be >= alpha
                        if best_score <= alpha_score:
                            # print( f'pruning min node score: {best_score} alpha: {alpha_score} ')
                            return (best_score, best_move)
                        beta_score = min([best_score, beta_score])
                    # print('at depth {} alpha {} betas {} '.format(depth, alpha_score, beta_score))
            # print('depth {} changed to best move {} and best score {} move {}'.format(depth, best_move, best_score, each_move))
        pass  # for loop
        # print('best move is ', best_move, best_score)
        return (best_score, best_move)

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

            """

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # call the helper function
        (score, move) = self.alphabeta_ply(
            game, depth, init_move=None, min_max=True)
    # print('score is {} and best move is {}'.format(score, move))
        return move
