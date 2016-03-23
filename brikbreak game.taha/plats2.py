
import turtle
from plats import *
from Brickclass import *
b2=plats(580,20,-0.1,6,1,"red")
b1=plats(-580,-20,-0.1,6,1,"yellow")
screen= turtle.getscreen()
turtle.tracer(0)
canvas=getcanvas() # the canvas is the area that the turtle is moving (the white background)
CANVAS_WIDTH = canvas.winfo_width() # here we get canvas(screen) width
CANVAS_HEIGHT = canvas.winfo_height() # here we get the canvas(screen) height
def get_screen_height():
	global CANVAS_HEIGHT
	return int(CANVAS_HEIGHT/2-5)
def get_screen_width():
	global CANVAS_WIDTH
	return int(CANVAS_WIDTH/2-10)
i=0

j=0
while(j<8):
	#print("here1")
	while(i<4):
		#print("here")
		b=Brick(-30*i,50*j,2,1,"yellow")
		b=Brick(-30*i,-50*j,2,1,"red")
		
		i+=1		
	j+=1
	i=0


while True :
	b1.move(get_screen_height(),get_screen_width())
	b2.move(get_screen_height(),get_screen_width())
	screen.update()


