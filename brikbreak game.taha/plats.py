from turtle import *
class plats(Turtle):
	def __init__(self,x,y,dy,width,height,color):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.color(color)
		self.width = width
		self.height = height
		
		self.dy=dy
		self.shape("square")
		self.shapesize(width,height,5)
		self.pu()
		self.goto(x,y)
	def move(self,height,width):
		self.goto(self.xcor(),self.ycor()+self.dy)
		if(self.ycor() <-height):
			self.dy=0
