def create_new_game_state():
    """
    Create and return a new game state object for Rotating Ultimate Tic-Tac-Toe.

    Returns:
        dict (or any custom object/structure you prefer):
            A data structure representing the entire game state.
            This should contain:
            - A 3x3 representation of sub-boards.
            - Each sub-board (3x3) contains small boards or cells.
            - Current player's mark ('X' or 'O').
            - Any additional metadata (e.g., forced sub-board, etc.).
    """
    pass


def place_move(game_state, player, global_subboard_row, global_subboard_col, local_row, local_col):
    """
    Place a mark (X or O) on the specified local cell of a sub-board.

    Args:
        game_state: The data structure holding current game info.
        player (str): 'X' or 'O'.
        global_subboard_row (int): 0, 1, or 2 indicating which sub-board row in the big board.
        global_subboard_col (int): 0, 1, or 2 indicating which sub-board column in the big board.
        local_row (int): 0, 1, or 2 indicating row inside that 3x3 sub-board.
        local_col (int): 0, 1, or 2 indicating column inside that 3x3 sub-board.

    Returns:
        None
    """
    pass


def rotate_subboard(game_state, global_subboard_row, global_subboard_col, clockwise=True):
    """
    Rotate the specified sub-board by 90 degrees (clockwise or counterclockwise).

    Args:
        game_state: The data structure holding current game info.
        global_subboard_row (int): Which sub-board row (0..2) in the big board.
        global_subboard_col (int): Which sub-board column (0..2) in the big board.
        clockwise (bool): If True, rotate 90° clockwise; otherwise 90° counterclockwise.

    Returns:
        None
    """
    pass


def check_small_board_winner(game_state, global_subboard_row, global_subboard_col):
    """
    Check if a particular 3x3 sub-board has a winner (X or O) or is tied.

    Args:
        game_state: The data structure holding current game info.
        global_subboard_row (int): Which sub-board row (0..2).
        global_subboard_col (int): Which sub-board column (0..2).

    Returns:
        str or None:
            'X' if X has won this sub-board,
            'O' if O has won this sub-board,
            'T' if it's a tie,
            or None if it's still undecided.
    """
    pass


def update_subboard_status(game_state):
    """
    Update the status of all sub-boards in the big board. 
    For each sub-board, set whether it's claimed by X, O, tied, or still active.

    Args:
        game_state: The data structure holding current game info.

    Returns:
        None
    """
    pass


def check_big_board_winner(game_state):
    """
    Check if there's a winner (X or O) on the overall 3x3 big board.

    Args:
        game_state: The data structure holding current game info.

    Returns:
        str or None:
            'X' if X has captured three sub-boards in a row (or column/diagonal),
            'O' if O has captured three sub-boards in a row,
            or None if there's no overall winner yet.
    """
    pass


def get_forced_subboard(game_state, local_row, local_col):
    """
    Given the local cell (row, col) that a player just played in, determine
    which sub-board the opponent must play in next (if that sub-board is still active).
    If that sub-board is already decided, the opponent may choose any open sub-board.

    Args:
        game_state: The data structure holding current game info.
        local_row (int): 0..2, the row of the local cell just used.
        local_col (int): 0..2, the column of the local cell just used.

    Returns:
        tuple or None:
            (forced_row, forced_col) if there's a forced sub-board,
            or None if there's no forced board (meaning the next player can go anywhere).
    """
    pass


def is_game_over(game_state):
    """
    Check if the game is completely over, either by a big board winner or a global tie.

    Args:
        game_state: The data structure holding current game info.

    Returns:
        bool: True if the game has ended, otherwise False.
    """
    pass


def get_winner(game_state):
    """
    Retrieve the overall winner (X or O) if one exists.

    Args:
        game_state: The data structure holding current game info.

    Returns:
        str or None:
            'X' if X has won,
            'O' if O has won,
            or None if no winner exists yet (including a tie).
    """
    pass


def display_game_state(game_state):
    """
    (Optional) Print or otherwise render the current game state.
    You can make this a no-op or a placeholder for UI/printing logic.

    Args:
        game_state: The data structure holding current game info.

    Returns:
        None
    """
    pass


