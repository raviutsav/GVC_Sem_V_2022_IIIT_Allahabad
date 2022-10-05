
#Q1 GVC: Transformation
# Create and rotate a triangle about the origin


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

window = 0                                             # glut window number
width, height = 500, 500                               # window size

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
                        
def draw_triangle(x1, y1, x2, y2, x3, y3):
    
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
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
    To rotate the triangle about the origin.

    glRotatef() function rotate around the origin
    
    Steps to follow for rotation the triangle about fix point
      
    The first argument of glRotatef() is the angle of rotation
    and second, third, fouth is the direction of rotation
    '''
                               
    glRotatef(-20.0, 0.0, 0.0, 1.0) 
    draw_triangle(200, 300, 250, 350, 300, 300)
    
    glutSwapBuffers()                                  # important for double buffering
   

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Q1")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()  
