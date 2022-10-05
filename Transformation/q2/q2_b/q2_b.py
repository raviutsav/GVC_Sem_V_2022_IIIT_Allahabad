
#Q2 Create a hut and perform the following transformations on it.

# (ii) Scale by 0.5 (fixed point scaling)


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

window = 0                                             # glut window number
width, height = 700, 700                               # window size

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
    
def draw_door(x1, y1, x2, y2, x3, y3, x4, y4):
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0.3)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

def draw_triangle(x1, y1, x2, y2, x3, y3):
    
    glBegin(GL_TRIANGLES)
    glColor3f(0.1, 0.2, 0.3)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

def draw():                                            	# ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 	# clear the screen
    glLoadIdentity()                                   	# reset position
    refresh2d(width, height)						   	# set mode to 2d
    	
    
    glColor3f(1.0, 0.0, 1.0)                           	# set color to blue
    glMatrixMode(GL_MODELVIEW)                          # To operate on Model-View matrix
    glLoadIdentity();               					# Reset the model-view matrix
    
    
    
    '''
    
    glScalef() function takes first value as scalling in x
    second argument as scalling in y
    third argument as scalling in z
    
    '''
    glScalef(0.5, 0.5, 0.5)                       
    draw_quad(200, 200, 200, 300, 300, 300, 300, 200)
    draw_door(240, 200, 240, 260, 260, 260, 260, 200)
    draw_triangle(200, 300, 250, 350, 300, 300)
    
    glutSwapBuffers()                                  # important for double buffering
   

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Q2")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()  
