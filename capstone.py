# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import math

# Create Classes
class Player(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.shapesize(stretch_wid=1, stretch_len=3, outline=None)
        
    def motion(self, event):
    	x1 = self.xcor()
    	y1 = self.ycor()
    	
    	x2, y2 = event.x, event.y
    	x2 -= 400
    	y2 -= 300
    	
    	angle = math.atan2(y2 - y1, x2 - x1) * -180 / math.pi;
    	self.setheading(angle)
        
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
player = Player("arrow", "green", 0, 0)
goal = Goal("square", "red", 50, -100)
ball = Ball("circle", "white", -387, 50)

# Set Keyboard Bindings

# Set Mouse Motion Bindings
canvas = spgl.turtle.getcanvas()
canvas.bind('<Motion>', player.motion)

while True:
    # Call the game tick method
    game.tick()
    