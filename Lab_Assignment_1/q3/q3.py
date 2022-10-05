
# Name: Ravi Utsav
# Roll: IIT2020504

#Q3 GVC Lab Assignment

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

window = 0                                             # glut window number
width, height = 1000, 500                               # window size

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()

def draw_circle(posx, posy, radius, sides):

	glBegin(GL_POINTS)
	for i in range(sides):
		cosine = radius * cos(i * 2 * pi/sides) + posx		#drawing the circle in parameter form,
															# for a circle whose radius is R and center position is cx, cy
															# then parameter form of such circle is x = R*cos(theta) + cx, y = R*sin(theta)*cy
															# here theta is variable which will be different for all the points.
		sine = radius * sin(i * 2 * pi/sides) + posy
		glVertex2f(cosine, sine)
	glEnd()
	
def draw_half_circle(posx, posy, radius, sides):

	glBegin(GL_POINTS)
	for i in range(sides//2):
		cosine = radius * cos(i *2* pi/sides) + posx
		sine = radius * sin(i *2* pi/sides) + posy
		glVertex2f(cosine, sine)
	glEnd()

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)						   # set mode to 2d
    
    
    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    draw_circle(200, 85, 50, 1000)
    draw_circle(600, 85, 50, 1000)
    draw_half_circle(200, 85, 55, 1000)
    draw_half_circle(600, 85, 55, 1000)
    glBegin(GL_LINES)
    glVertex2f(70, 85)
    glVertex2f(145, 85)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(255, 85)
    glVertex2f(545, 85)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(655, 85)
    glVertex2f(830, 85)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(70, 85)
    glVertex2f(70, 160)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(70, 160)
    glVertex2f(160, 220)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(200, 350)
    glVertex2f(160, 220)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(185, 210)
    glVertex2f(225, 340)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(185, 210)
    glVertex2f(370, 210)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(200, 350)
    glVertex2f(550, 350)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(600, 220)
    glVertex2f(550, 350)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(535, 340)
    glVertex2f(585, 210)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(585, 210)
    glVertex2f(380, 210)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(600, 220)
    glVertex2f(830, 160)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(830, 85)
    glVertex2f(830, 160)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(0, 30)
    glVertex2f(1000, 30)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(225, 340)
    glVertex2f(370, 340)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(380, 340)
    glVertex2f(535, 340)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(370, 340)
    glVertex2f(370, 210)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(380, 340)
    glVertex2f(380, 210)
    glEnd()
   	
    glutSwapBuffers()                                  # important for double buffering
   

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Q3_IIT2020504")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()  
