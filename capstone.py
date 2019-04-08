# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import math
import random

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
        self.setheading(0)
        
        colors = ["blue", "green", "purple", "orange"]
        color = random.choice(colors)
        self.color(color)


    def is_near(self, x1, y1, x2, y2):
    	d = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
    	if d < 20:
    		return True
    	else:
    		return False
    		        
    # Move the ball
    def move(self):
    	self.forward(4)
    	
    	# Check for collisions 
    	if self.is_near(self.xcor(), self.ycor(), 250, 200):
    		self.setheading(270)
    		
    	elif self.is_near(self.xcor(), self.ycor(), 250, -180):
    		self.setheading(180)
    	
    	elif self.is_near(self.xcor(), self.ycor(), -280, -180):
    		self.setheading(90)
    	
    	elif self.is_near(self.xcor(), self.ycor(), -280, 130):
    		self.setheading(0)
    		
    	elif self.is_near(self.xcor(), self.ycor(), 160, 130):
    		self.setheading(270)
    		
    	elif self.is_near(self.xcor(), self.ycor(), 160, -100):
    		self.goto(150, -100)
    
# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "Rainbow Pop by Elno", 0)

# Create Sprites
player = Player("arrow", "green", 0, 0)
goal = Goal("square", "red", 150, -100)
ball = Ball("circle", "white", -387, 200)

balls = [ball]

# Set Keyboard Bindings

# Set Mouse Motion Bindings
canvas = spgl.turtle.getcanvas()
canvas.bind('<Motion>', player.motion)

while True:
	# Call the game tick method
	game.tick()
	for ball in balls:
		ball.move()
		
	# Add a new ball
	if random.randint(0, 1000) > 990:	
		ball = Ball("circle", "white", -387, 200)
		balls.append(ball)
    