# The game_object class
- Objects for this class are objects in the game i.e. spaceships, enemies, bullets
- the delete method deletes the object from the class by removing it from the appropriate array (bullets, objects, enemies), and replaces their images with black background

# The create_bullet() module 
- creates a new bullet with x and y coordinate same as that of the spaceship at that time and adds it to the bullets array

# The create_enemy() module 
- creates a new enemy with random x-coordinate and at y = 0 and adds it to the enemies array

# The game_logic() module
- Checks for collision between bullets and spaceships rectangles (through pygame.Rect.colliderect method)
- The enemy that takes the hit from the bullet dies (deleted) and so is the bullet

# The main() module
- Main part of the game
- checks for events occuring
- for KEYDOWN event (keyboard presseed), when arrows (LEFT, RIGHT) or (A, D) are pressed, the moveLeft and moveRight are set to True respectively
- when moveLeft is True, the spaceship moves to the left for every iteration of the while loop
- when moveRight is True, the spaceship moves to the right for every iteration of the while loop
- The code is such that both can't be True at the same time
- To stop movement, the user has to let go of the keys to trigger the KEYUP event.
- If A or LEFT key is let go, the moveLeft is set to False, and if D or RIGHT key is let go, the moveRight is set to False
- When user presses the key F, the create_bullet() module is called
- If a bullet goes above the screen rect.top <= 0, it is deleted
- the background is rendered before rendering every object from the objects array

# The game_init() module
- Loads the initial screen
- Changes the value of currentSelect based on user input for GUI
- Calls the drawInitialScreen module accordingly

# The drawInitialScreen() module
- Code to draw the initial screen (options screen)
- What is displayed depends on the value of currentSelect

# The pause() module:
- Called when user presses the ESCAPE button
- Changes values of pauseSelect according to user input and calls the drawPauseScreen() module

# The drawPauseScreen() module
- Called from the pause() module
- Depending on the value of pauseSelect, it changes the current item selected in the pause-menu

# The changeScore() module
- Called initially to set `score_text` variable to initial score `0`
- Whenever a bullet hits the enemy, it is called again after `score` is changed to display the changed score
- `score_text` and `score_text_rect` are global variables so that they can be used inside `main` module.

# The changeLife() module
- Similar to the `changeScore()` module
- Called initially to set `life_text` variable to initial life `5`
- Whenever an enemy is missed, it is called again after `life` is changed to display the changed life.
- `life_text` and `life_text_rect` are global variables so that they can be used inside `main` module.


# User Events
- A logic event is fired every 50 ms, and in the main() module, this event triggers the game_logic() function to check any collisions
- A move event is fired every 100ms, and in the main() module, this event triggers the movement of enemy towards the earth
- An enemyCreate event is fired every 3000ms, and in the main() moduke, this event triggers the create_enemy() module

# General pygame
- https://www.pygame.org/docs/
- Working of computer graphics: https://www.pygame.org/docs/tut/MoveIt.html


# Images:
![Initial Screen](https://i.imgur.com/cezdTrM.png)
![Earth and Spaceship](https://i.imgur.com/6BTk94F.png)
![Pause Screen](https://i.imgur.com/S0AYJGY.png)
![Laser, Enemy](https://i.imgur.com/dBwUtLr.png)
