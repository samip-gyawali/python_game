# The game_object class
- Objects for this class are objects in the game i.e. spaceships, enemies, bullets
- the `delete()` method deletes the object from the class by removing it from the appropriate array (bullets, objects, enemies), and replaces their images with black background

# The create_bullet() module 
- creates a new bullet with x and y coordinate same as that of the spaceship at that time and adds it to the bullets array

# The create_enemy() module 
- creates a new enemy with random x-coordinate and at y = 0 and adds it to the enemies array

# The game_logic() module
- Checks for collision between bullets and spaceships rectangles (through `pygame.Rect.colliderect` method)
- The enemy that takes the hit from the bullet dies (deleted) and so is the bullet

# The main() module
- Main part of the game
- checks for events occuring
- for `KEYDOWN` event (keyboard presseed), when arrows (LEFT, RIGHT) or (A, D) are pressed, the `moveLeft` and `moveRight` property for the spaceship are set to True       respectively
- when `moveLeft` is True, the spaceship moves to the left for every iteration of the while loop
- when `moveRight` is True, the spaceship moves to the right for every iteration of the while loop
- The code is such that both can't be True at the same time
- To stop movement, the user has to let go of the keys to trigger the `KEYUP` event.
- If A or LEFT key is let go, the moveLeft is set to False, and if D or RIGHT key is let go, the moveRight is set to False
- When user presses the key `F`or `<space>`, the `create_bullet()` module is called
- If a bullet goes above the screen `rect.top <= 0`, it is deleted
- the background is rendered before rendering every object from the objects array

# The game_init() module
- Loads the initial screen
- Changes the value of `currentSelect` based on user input for GUI
- Calls the `drawInitialScreen` module accordingly

# The drawInitialScreen() module
- Code to draw the initial screen (options screen)
- What is displayed depends on the value of `currentSelect`

# The pause() module:
- Called when user presses the ESCAPE button
- Changes values of `pauseSelect` according to user input and calls the `drawPauseScreen()` module

# The drawPauseScreen() module
- Called from the `pause()` module
- Depending on the value of `pauseSelect`, it changes the current item selected in the pause-menu

# The changeScore() module
- Called initially to set `score_text` variable to initial score `0`
- Whenever a bullet hits the enemy, it is called again after `score` is changed to display the changed score
- `score_text` and `score_text_rect` are global variables so that they can be used inside `main` module.

# The changeLife() module
- Similar to the `changeScore()` module
- Called initially to set `life_text` variable to initial life `5`
- Whenever an enemy is missed, it is called again after `life` is changed to display the changed life.
- `life_text` and `life_text_rect` are global variables so that they can be used inside `main` module.

# The setHighScore() module:
- the `highScore` variable is set at the beginning of the program. If `high_score.txt` file exists, `highScore` is set to the current value
- If it doesn't exist, the `high_score.txt` file is created and `highScore` is set to `0`
- When game is over this module is called
- Comparing the current value of `score` with `highScore`, it changes the `highScore` if required.

# The final() module:
- Called after game is over
- If a user exits or presses any key, the game is closed

# The drawExitScreen() module:
- Displays the contents of exit screen

# User Events
- A logic event is fired every 50 ms, and in the `main()` module, this event triggers the `game_logic()` function to check any collisions
- A move event is fired every 100ms, and in the `main()` module, this event triggers the movement of enemy towards the earth
- An `enemyCreate` event is fired, and in the `main()` module, this event triggers the `create_enemy()` module

# enemyCreate Event
- The `enemyCreateTime` variable dictates the interval in which the enemyCreate Event is triggered
- The `makeGameHarder` is increased any time a bullet hits an enemy
- Everytime the `makeGameHarder` variable hits the value 40, the `enemyCreaateTime` is divided by `1.1`, and enemyCreate event timer is restarted with this changed value
- So, everytime the player makes 4 kills, the game gets harder as enemies spawn faster


# General pygame
- https://www.pygame.org/docs/
- Working of computer graphics: https://www.pygame.org/docs/tut/MoveIt.html


# Images:
![Initial Screen](https://i.imgur.com/cezdTrM.png)
![Earth and Spaceship](https://i.imgur.com/6BTk94F.png)
![Pause Screen](https://i.imgur.com/S0AYJGY.png)
![Laser, Enemy](https://i.imgur.com/dBwUtLr.png)
![Score, Life](https://i.imgur.com/Ujl8KKU.png)
