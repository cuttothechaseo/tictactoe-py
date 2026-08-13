# Tic-Tac-Toe — Function Structure

**Goal:** Build a terminal-based Tic-Tac-Toe game where the player plays against a bot.

## `create_board()`

**Responsibility:** Create the initial game board.

* Creates the 9 available positions.
* Returns the board.

---

## `display_board(board)`

**Responsibility:** Display the current state of the board.

* Receives the board.
* Prints it as a 3×3 Tic-Tac-Toe grid.
* Does not change the board.

---

## `get_player_move(board)`

**Responsibility:** Handle the human player's turn.

* Receives the current board.
* Asks the player to choose a position.
* Returns the player's chosen position.

---

## `get_bot_move(board)`

**Responsibility:** Decide the bot's move.

* Receives the current board.
* Examines the available positions.
* Chooses a position.
* Returns the bot's chosen position.

The bot logic can start simple and become smarter later.

---

## `validate_move(board, position)`

**Responsibility:** Determine whether a proposed move is legal.

* Receives the board and proposed position.
* Checks whether the position exists and is available.
* Returns whether the move is valid.

---

## `make_move(board, position, symbol)`

**Responsibility:** Update the board.

* Receives the board.
* Receives the chosen position.
* Receives the symbol (`X` or `O`).
* Places that symbol on the board.

---

## `check_winner(board)`

**Responsibility:** Determine whether someone has won.

* Receives the current board.
* Checks rows.
* Checks columns.
* Checks diagonals.
* Returns the result.

---

## `check_draw(board)`

**Responsibility:** Determine whether the game ended in a draw.

* Receives the board.
* Checks whether there are any remaining available positions.
* Returns the result.

---

## `play_game(board)`

**Responsibility:** Orchestrate the game.

Repeatedly coordinates the other functions:

**Player turn**

* Display board
* Get player move
* Validate move
* Make player move
* Check winner
* Check draw

**Bot turn**

* Get bot move
* Make bot move
* Check winner
* Check draw

Then repeats until the game ends.

---

## `main()`

**Responsibility:** Start the program.

* Creates the board.
* Passes the board into the game.
* Calls `play_game()`.

---

## Overall Flow

**Main**

→ Create board

→ Play game

→ Player move

→ Update board

→ Check game state

→ Bot move

→ Update board

→ Check game state

→ Repeat

→ Game over
