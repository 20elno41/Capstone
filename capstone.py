# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import math
import random
import time

# Create Classes
class GalaxyCrash(spgl.Game):
	def __init__(self, x, y, color, title, seconds):
		spgl.Game.__init__(self, x, y, color, title, seconds)
		
	def click(self, x, y):
		shooting_ball.shoot()
		
class Player(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.shapesize(stretch_wid = 1, stretch_len = 3, outline = None)
        
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
    
        colors = ["dodgerblue", "green", "purple", "orange"]
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
    	self.forward(3)
    	
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
    
class ShootingBall(Ball):
	def __init__(self, shape, color, x, y):
		Ball.__init__(self, shape, color, x, y)
		colors = ["dodgerblue", "green", "purple", "orange"]
		color = random.choice(colors)
		self.color(color)
		self.state = "home"
        
	def shoot(self):
		if self.state == "home":
			self.goto(0, 0)
			self.setheading(player.heading())
			self.state = "move"
		
	def change_color(self):
		colors = []
		
		for ball in balls:
			colors.append(ball.color()[0])
		
		if len(colors) > 0:	
			color = random.choice(colors)
			self.color(color)
		else:
			self.color("blue")
		
	def move(self):	
		self.forward(18)
		
		# Check for border collision
		if self.xcor() > game.SCREEN_WIDTH / 2 or self.xcor() < game.SCREEN_WIDTH / -2:
			shooting_ball.change_color()
			shooting_ball.goto(0,0)
			shooting_ball.state = "home"
			
		if self.ycor() > game.SCREEN_WIDTH / 2 or self.ycor() < game.SCREEN_WIDTH / -2:
			shooting_ball.change_color()
			shooting_ball.goto(0,0)
			shooting_ball.state = "home"
		
	def tick(self):
		if self.state == "move":
			self.move()

# Initial Game setup
game = GalaxyCrash(800, 600, "black", "Galaxy Crash by Elno", 5)
game.frame = 1

# Create Sprites
player = Player("arrow", "white", 0, 0)
goal = Goal("black_hole.gif", "red", 150, -100)
ball = Ball("circle", "white", -387, 200)
shooting_ball = ShootingBall("circle", "white", 0, 0)

balls = [ball]

# Set Mouse Motion Bindings
canvas = spgl.turtle.getcanvas()
canvas.bind('<Motion>', player.motion)

# Set the Background Image
game.set_background("galaxy2.gif")

game_over = False

while True:
	# Call the game tick method
	game.tick()
	for ball in balls:
		ball.move()
		
		# Check if a ball hits the goal
		if game.is_collision(ball, goal):
			game_over = True
		
		# Check for collision with the shooting ball
		if game.is_collision(shooting_ball, ball) and shooting_ball.color() == ball.color():
			
			# Check for combos
			index = balls.index(ball)
			try:
				next = balls[index + 1]
				game.play_sound("blop.wav")
			except:
				pass
				
			try:
				next2 = balls[index + 2]
			except:
				pass
				
			try:
				previous = balls[index - 1]
			except:
				pass
			
			try:
				previous2 = balls[index - 2]
			except:
				pass
			
			try:
				if ball.color()[0] == next2.color()[0] and ball.distance(next2) < 50 and ball.color()[0] == next.color()[0]:
					balls.remove(next2)
					next2.color("black")
					next2.hideturtle()
			except:
				pass
				
			try:	
				if ball.color()[0] == previous2.color()[0] and ball.distance(previous2) < 50 and ball.color()[0] == previous.color()[0]:
					balls.remove(previous2)
					previous2.color("black")
					previous2.hideturtle()
			except:
				pass
				
			try:
				if ball.color()[0] == next.color()[0] and ball.distance(next) < 25:
					balls.remove(next)
					next.color("black")
					next.hideturtle()
			except:
				pass
			
			try:	
				if ball.color()[0] == previous.color()[0] and ball.distance(previous) < 25:
					balls.remove(previous)
					previous.color("black")
					previous.hideturtle()
			except:
				pass
			
			# Remove the ball from the screen
			if ball in balls: 
				ball.color("black")
				ball.hideturtle()
				balls.remove(ball)
			
			# Change shooting color
			shooting_ball.change_color()
			shooting_ball.goto(0,0)
			shooting_ball.state = "home"
		
	# Add a new ball
	if game.frame % 7 == 0 and game.frame <= 355:	
		ball = Ball("circle", "white", -387, 200)
		balls.append(ball)
	game.frame += 1
	
	# Game Over
	if game_over == True:
		game.set_background("game_over2.gif")
		game.update_screen()
		game.play_sound("explosion.wav")
		time.sleep(2)
		break
	
	# You Win
	if len(balls) == 0:
		game.set_background("you_win2.gif")
		game.update_screen()
		game.play_sound("win.wav")
		time.sleep(2)
		break