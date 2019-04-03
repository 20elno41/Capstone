# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl

# Create Classes
class Player(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        
class Goal(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        
class Ball(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "Rainbow Pop by Elno", 0)

# Create Sprites
player = Player("triangle", "green", 0, 0)
goal = Goal("square", "red", 50, -100)
ball = Ball("circle", "white", -387, 50)

# Create Labels

# Create Buttons

# Set Keyboard Bindings

while True:
    # Call the game tick method
    game.tick()
