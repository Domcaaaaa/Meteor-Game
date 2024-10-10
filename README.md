# Meteor Dodger Game

A simple Python game where you control a spaceship and dodge falling meteors. The game is built using the `play` library and features basic collision detection, score tracking, and game-over functionality.

## Table of Contents
- [Overview](#overview)
- [Gameplay](#gameplay)
- [Setup](#setup)
- [How to Play](#how-to-play)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Overview
In this game, the player maneuvers a spaceship to avoid meteors falling from the sky. The game keeps track of the player's score, which increases each time a meteor passes without colliding with the spaceship. When a collision occurs, the game displays a "Game Over" message, and the player has the option to restart.

## Gameplay
- **Player Control**: The player uses the **A** and **D** keys to move the spaceship left and right.
- **Meteor Speed**: The speed of falling meteors increases as the player's score goes up, making the game progressively more challenging.
- **Score**: The score is incremented for each meteor that the spaceship successfully dodges.
- **Game Over**: If the spaceship collides with a meteor, the game shows a "Game Over" screen, and the player can press **Q** to reset the game.

## Setup
### Prerequisites
- Python 3.x installed on your system.
- The `play` library, which you can install via pip:
  ```bash
  pip install play
  ```

### Running the Game
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/meteor-dodger-game.git
   cd meteor-dodger-game
   ```

2. Run the game:
   ```bash
   python game.py
   ```

3. The game window will open, and you can start playing by using the **A** and **D** keys to move the spaceship.

## How to Play
- Use the **A** key to move the spaceship left.
- Use the **D** key to move the spaceship right.
- Avoid the falling meteors; if a meteor touches your spaceship, the game will display "Game Over."
- Press **Q** to reset and restart the game when it's over.

## Notes
- **Assets**: Make sure that the images `space.jpg`, `spaceship.png`, and `meteor.png` are present in the same directory as `game.py`. These images are used for the background, spaceship, and meteors, respectively.
- **Difficulty**: The speed of the meteors increases as your score increases, adding an element of difficulty as the game progresses.
