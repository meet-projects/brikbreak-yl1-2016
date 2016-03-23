from turtle import *
class Brick(Turtle):
	def __init__(self,x,y,width,height,color):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.color(color)
		self.width = width
		self.height = height
		self.shape("square")
		self.shapesize(width,height,5)
		self.pu()
		self.goto(x,y)

	#self.goto(x-width/2, y+height/2)
	#self.pendown()
	#self.goto(x+width/2, y+height/2)
	#self.pendown()
	#self.goto(x+width/2 , y-height/2)
	#self.pendown()
	#self.goto(x-width/2 ,y-height/2)
	#self.pendown()
	#self.goto(x-width/2 , y+height/2)
	
