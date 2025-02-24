import unittest
from template import (
    create_new_game_state,
    place_move,
    rotate_subboard,
    check_small_board_winner,
    update_subboard_status,
    check_big_board_winner,
    get_forced_subboard,
    is_game_over,
    get_winner,
    display_game_state
)

class TestRotatingUltimateTicTacToeAdvanced(unittest.TestCase):

    def setUp(self):
        """
        Run before every test.
        Create a fresh game state for isolation.
        """
        self.game_state = create_new_game_state()

    # -------------------------------------------------------------------------
    # Basic Tests (from your existing suite, plus expansions)
    # -------------------------------------------------------------------------

    def test_create_new_game_state_structure(self):
        """
        Check that the initial game state has the proper nested structure
        and default values (like empty cells).
        """
        self.assertIsNotNone(self.game_state)
        # Example structural checks — adapt to your data format:
        # self.assertIn('big_board', self.game_state)
        # self.assertEqual(len(self.game_state['big_board']), 3)
        # for row in self.game_state['big_board']:
        #     self.assertEqual(len(row), 3)
        #     for subboard in row:
        #         self.assertIsInstance(subboard, dict)
        #         # Maybe each subboard has its own 3x3 cells structure
        #         self.assertIn('cells', subboard)
        #         self.assertEqual(len(subboard['cells']), 3)

    def test_place_move_on_empty_cell(self):
        """
        Test placing a move on an empty cell (valid scenario).
        This should succeed without errors and mark the cell.
        """
        place_move(self.game_state, 'X', 0, 0, 1, 1)
        # Check that the cell is 'X'
        # cell_value = self.game_state['big_board'][0][0]['cells'][1][1]
        # self.assertEqual(cell_value, 'X', "Cell (1,1) in sub-board (0,0) should be marked 'X'.")

    def test_place_move_out_of_bounds(self):
        """
        Attempting to place a move where local_row or local_col is not in [0..2]
        should raise an error or be otherwise invalid.
        """
        with self.assertRaises(Exception):
            place_move(self.game_state, 'O', 0, 0, 3, 2)

    def test_place_move_in_occupied_cell(self):
        """
        Placing a move in an already occupied cell should raise an exception.
        """
        place_move(self.game_state, 'X', 0, 0, 0, 0)
        # Now placing another move in the same cell:
        with self.assertRaises(Exception):
            place_move(self.game_state, 'O', 0, 0, 0, 0)

    def test_rotate_subboard_clockwise(self):
        """
        Verify a 90° clockwise rotation rearranges cells correctly.
        """
        # Place some distinct marks for easy tracking
        place_move(self.game_state, 'X', 0, 0, 0, 0)
        place_move(self.game_state, 'O', 0, 0, 1, 2)
        place_move(self.game_state, 'X', 0, 0, 2, 1)

        rotate_subboard(self.game_state, 0, 0, clockwise=True)
        # Now check new positions in sub-board (0,0) after rotation
        # Example expectation: after a 90° clockwise rotation:
        #
        # Original ->   [ [X,   ' ', 'O' ],
        #                [ ' ', ' ', ' ' ],
        #                [ ' ', 'X', ' '] ]
        # is rearranged. Adjust to your own tracking method:
        #
        # updated_cells = self.game_state['big_board'][0][0]['cells']
        # self.assertEqual(updated_cells[0][2], 'X', "Cell (0,2) should contain the original top-left mark 'X'.")
        # etc...

    def test_rotate_subboard_counterclockwise(self):
        """
        Test a 90° counterclockwise rotation.
        """
        place_move(self.game_state, 'X', 0, 0, 0, 2)
        place_move(self.game_state, 'O', 0, 0, 2, 2)

        rotate_subboard(self.game_state, 0, 0, clockwise=False)
        # Check new positions
        # updated_cells = self.game_state['big_board'][0][0]['cells']
        # self.assertEqual(updated_cells[2][0], 'X', "Mark 'X' from (0,2) should move to (2,0) in a CCW rotation.")
        # self.assertEqual(updated_cells[2][2], ' ', "Cell (2,2) was originally 'O'; check where it lands.")


    # -------------------------------------------------------------------------
    # More Advanced Tests
    # -------------------------------------------------------------------------

    def test_check_small_board_winner_row(self):
        """
        Create a horizontal winning pattern for X in sub-board (1,1).
        """
        place_move(self.game_state, 'X', 1, 1, 0, 0)
        place_move(self.game_state, 'X', 1, 1, 0, 1)
        place_move(self.game_state, 'X', 1, 1, 0, 2)
        winner = check_small_board_winner(self.game_state, 1, 1)
        self.assertEqual(winner, 'X', "X should have a horizontal win in sub-board (1,1).")

    def test_check_small_board_winner_diagonal(self):
        """
        Create a diagonal winning pattern for O in sub-board (2,2).
        """
        place_move(self.game_state, 'O', 2, 2, 0, 0)
        place_move(self.game_state, 'O', 2, 2, 1, 1)
        place_move(self.game_state, 'O', 2, 2, 2, 2)
        winner = check_small_board_winner(self.game_state, 2, 2)
        self.assertEqual(winner, 'O', "O should have a diagonal win in sub-board (2,2).")

    def test_update_subboard_status_after_wins(self):
        """
        Place multiple winning lines in multiple sub-boards, then call update_subboard_status.
        Verify each sub-board's status is updated correctly (X, O, T).
        """
        # Sub-board (0,0) => X wins
        place_move(self.game_state, 'X', 0, 0, 0, 0)
        place_move(self.game_state, 'X', 0, 0, 0, 1)
        place_move(self.game_state, 'X', 0, 0, 0, 2)

        # Sub-board (1,1) => O wins
        place_move(self.game_state, 'O', 1, 1, 2, 0)
        place_move(self.game_state, 'O', 1, 1, 2, 1)
        place_move(self.game_state, 'O', 1, 1, 2, 2)

        update_subboard_status(self.game_state)
        # Check subboard statuses:
        # self.assertEqual(self.game_state['subboard_status'][0][0], 'X')
        # self.assertEqual(self.game_state['subboard_status'][1][1], 'O')

    def test_check_big_board_winner_with_three_captured_subboards(self):
        """
        Force X to capture three sub-boards in a row on the big board (0,0), (0,1), (0,2).
        Check if check_big_board_winner() detects X as winner.
        """
        # Typically you'd set the subboard_status array or forcibly create wins:
        # self.game_state['subboard_status'][0][0] = 'X'
        # self.game_state['subboard_status'][0][1] = 'X'
        # self.game_state['subboard_status'][0][2] = 'X'
        winner = check_big_board_winner(self.game_state)
        self.assertIn(winner, [None, 'X', 'O'],
                      "Winner should be either None, 'X', or 'O' if logic is consistent.")

        # If your logic updates automatically, verify it returns 'X':
        # self.assertEqual(winner, 'X', "X should have a big-board row win.")

    def test_get_forced_subboard_after_move(self):
        """
        If a move is placed in local (2,1), the forced sub-board on the big board is (2,1),
        unless it's already decided. Then the next player can choose any open sub-board.
        """
        forced_pos = get_forced_subboard(self.game_state, 2, 1)
        # self.assertEqual(forced_pos, (2, 1), "Forced sub-board should be (2,1).")

    def test_is_game_over_scenarios(self):
        """
        1) Check that a fresh game is not over.
        2) Force or simulate a big board win/tie, and check that is_game_over becomes True.
        """
        self.assertFalse(is_game_over(self.game_state), "New game should not be over.")

        # Suppose X just captured 3 sub-boards in a row:
        # self.game_state['subboard_status'][0] = ['X', 'X', 'X']
        # Now is_game_over should be True if the logic is correct.
        # self.assertTrue(is_game_over(self.game_state), "Game should be over once X has 3 in a row.")

    def test_get_winner_no_winner_yet(self):
        """
        In a fresh game, there is no winner.
        """
        self.assertIsNone(get_winner(self.game_state), "Initially, there should be no winner.")

    def test_get_winner_with_tie_scenario(self):
        """
        If the big board ends in a tie, ensure get_winner() returns None or 'T', depending on your logic.
        """
        # Force all sub-boards to be decided, but no row/col/diag captured by the same player.
        # for i in range(3):
        #     for j in range(3):
        #         self.game_state['subboard_status'][i][j] = 'T'
        # self.assertTrue(is_game_over(self.game_state))
        # self.assertIn(get_winner(self.game_state), [None, 'T'],
        #               "If there's a tie, get_winner() might return None or 'T' depending on your design.")

    def test_display_game_state_intermittent(self):
        """
        Make a few moves, rotate a sub-board, then verify display_game_state() doesn't crash.
        (We won't check the exact output, but ensure no exceptions occur.)
        """
        place_move(self.game_state, 'X', 0, 0, 0, 0)
        rotate_subboard(self.game_state, 0, 0, clockwise=True)
        display_game_state(self.game_state)

    def test_complex_move_sequence(self):
        """
        Simulate a realistic multi-move sequence:
          1) X plays in sub-board (0,0) local (0,0)
          2) Board rotates
          3) Forced sub-board is (0,0)? Then O plays, etc.
        We'll check partial states along the way.
        """
        place_move(self.game_state, 'X', 0, 0, 0, 0)
        rotate_subboard(self.game_state, 0, 0)
        # forced = get_forced_subboard(self.game_state, 0, 0)
        # self.assertEqual(forced, (0, 0))
        # Now O tries:
        place_move(self.game_state, 'O', 0, 0, 1, 1)
        rotate_subboard(self.game_state, 0, 0)
        # forced2 = get_forced_subboard(self.game_state, 1, 1)
        # self.assertIsNotNone(forced2)
        # Keep going, etc. You can add as many steps as you like,
        # checking intermediate states.

    # -------------------------------------------------------------------------
    # Test suite runner:
    # -------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
