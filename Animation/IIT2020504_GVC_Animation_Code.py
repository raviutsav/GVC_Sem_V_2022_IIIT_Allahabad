
# name : Ravi Utsav
# roll : IIT2020504

# Chair falling on table animation

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

window = 0                                             # glut window number
width, height = 1000, 500                              # window size
pos = 0
degree = 0.0
def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def draw_quad(x1, y1, x2, y2, x3, y3, x4, y4):

    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

def draw_table_quad(x1, y1, x2, y2, x3, y3, x4, y4):

    glColor3f(0.59, 0.3, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

def draw_chair_quad(x1, y1, x2, y2, x3, y3, x4, y4):
    glColor3f(0.53, 0.8, 0.92)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

def draw():                                            	# ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 	# clear the screen
    glLoadIdentity()                                   	# reset position
    refresh2d(width, height)				# set mode to 2d
    	
    
    glColor3f(0.5, 0.5, 0.5)                           	# set color to blue
    glMatrixMode(GL_MODELVIEW)                          # To operate on Model-View matrix
    glLoadIdentity();               			# Reset the model-view matrix
    
    global pos
    global degree
    global flag
    x_prime = (730 - 660)*cos((pi * degree)/180) - ((270 - 31)*sin((pi * degree)/180)) + 660
    y_prime = (730 - 660)*sin((pi * degree)/180) + (270 - 31)*cos((pi * degree)/180) + 31
    
    x_prime_2 = (730 - 660)*cos((pi * degree)/180) - ((31 - 31)*sin((pi * degree)/180)) + 660
    y_prime_2 = (730 - 660)*sin((pi * degree)/180) + (31 - 31)*cos((pi * degree)/180) + 31
    slope1 = (x_prime_2 - (pos+570))/(y_prime_2 -(pos+230))
    slope2 = (x_prime - (pos+570))/(y_prime - (pos+230))
    
    if degree > 90.0:
    	return
    
    if abs(slope1 - slope2) <= 0.5:
    	pos -= ((180 * 0.5 * pi)/(180 * (sin(pi/2 - ((pi * degree)/180))**2)) + 1)
    	
    draw_quad(10, 10, 10, 30, 990, 30, 990, 10)             
    draw_table_quad(pos+200, 31, pos+220, 31, pos+220, 210, pos+200, 210)
    draw_table_quad(pos+550, 31, pos+570, 31, pos+570, 210, pos+550, 210)
    draw_table_quad(pos+200, 210, pos+570, 210, pos+570, 230, pos+200, 230)
    
    
    glTranslatef(660, 31, 0)                       
    glRotatef(degree, 0.0, 0.0, 1.0)
    glTranslatef(-660, -31, 0)
    draw_chair_quad(660, 31, 680, 31, 680, 130, 660, 130)
    draw_chair_quad(660, 130, 730, 130, 730, 150, 660, 150)
    draw_chair_quad(730, 31, 750, 31, 750, 270, 730, 270)
    
    degree += 0.2
    flag = 0
    glutSwapBuffers()                                  # important for double buffering
   

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("GVC_animation_IIT2020504")  # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()  
