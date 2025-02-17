

# tiktak

"Your task is to ask Gemini 1.5 flash to code a tic-tac-toe game in python using the outline template provided in this repo. which will be evaluated using unit tests. Copy and paste in the program and don’t change anything."


**Rotating Ultimate Tic-Tac-Toe** is a wild twist on the classic “Ultimate” (or “Super”) Tic-Tac-Toe. Here’s how it works:

1. **Board Setup**  
   - You have a 3×3 “big board,” where each cell is itself a 3×3 “small board.”  
   - This means there are 9 small boards, each with 9 cells, for a total of 81 playable spaces.

2. **Standard Ultimate Rules**  
   - On your turn, you place your mark (X or O) in one of the small boards.  
   - Wherever you place your mark inside that small board (say in row _r_, column _c_), you *force* your opponent to play their next move in the big board’s sub-board at _(r, c)_, if that sub-board is still active.

3. **The Rotating Twist**  
   - After you place your mark in any small board, you immediately **rotate that entire small board by 90°** (clockwise or counterclockwise).  
   - All existing marks within that small board pivot to their new positions.

4. **Winning a Small Board**  
   - If you get three in a row in a small board, you claim it with your mark (like normal Tic-Tac-Toe). A claimed (or tied) board is considered “decided” and can’t be won again.

5. **Winning the Big Board**  
   - Each small board you claim acts as your mark (X or O) in the big board’s 3×3 grid.  
   - The first player to claim three small boards in a row, column, or diagonal **wins the entire game**.

**In short**: Every time you make a move, you rotate the small board you just played in, scrambling the layout. This constant shifting adds a new layer of strategy (and chaos!) to the already challenging Ultimate Tic-Tac-Toe, demanding quick thinking and sharp spatial awareness to come out on top.



