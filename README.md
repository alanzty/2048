<<<<<<< HEAD
# 2048
=======
# 2048 Game - README

## Overview

This is a Python implementation of the popular 2048 game using Pygame for the graphical interface. The goal of the game is to achieve highest score and tile possible with 0 undo. You can use the undo for practice. 

## Installation

1. **Install the required dependencies:**
    ```bash
    pip install numpy pygame
    ```

## How to Play

### Controls

- **Arrow Keys:** Move the tiles in the respective direction (left, right, up, down).
- **Spacebar:** Undo the last move.
- **R Key:** Reset the game.
- **Escape Key:** Quit the game.

### Objective

Slide the tiles on the board to combine them and create a tile with the number 2048. The game ends when no more moves are possible.

### Rules

- **Adding Tiles:** Each move adds a new tile (2 or 4) to the board at a random empty position.
- **Combining Tiles:** When two tiles with the same number collide while moving, they merge into a tile with the total of their values.
- **Undo:** You can undo the last move by pressing the Spacebar.

## Running the Game

1. **Execute the script:**
    ```bash
    python game_engine.py
    ```

2. **Enjoy the game!**

## Features

- **Scoring System:** Track your score as you combine tiles.
- **Undo Functionality:** Undo your last move with the Spacebar.
- **Reset Functionality:** Reset the game with the R key.
- **Game Over Detection:** The game will notify you when no more moves are possible.

>>>>>>> initial commit
