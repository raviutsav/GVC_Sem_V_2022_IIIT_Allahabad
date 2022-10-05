

# Name: Ravi Utsav
# Roll: IIT2020504

#Q2 GVC Lab Assignment


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

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)						   # set mode to 2d
    
    
    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    draw_circle(250, 250, 100, 3000)
    				   # made the circle with radius(R) 100, and center x, y coordinate as 250, 250
    theta = -pi/10
    prev_x = 100*cos(theta) + 250
    prev_y = 100*sin(theta) + 250
    
    for i in range(20):
    	glBegin(GL_LINES)   							# the pattern in this question is that, connect two points with a line, which are
    													# separated by 144 degree = 4*pi/5 on the circumference of the circle
    	theta = theta + (4*pi/5)
    	new_x = 100*cos(theta) + 250
    	new_y = 100*sin(theta) + 250
    	
    	glVertex2f(prev_x, prev_y)
    	glVertex2f(new_x, new_y)
    	prev_x = new_x
    	prev_y = new_y
    	glEnd()
    	
    theta = pi/10										# repeat the above pattern with diiferent starting point, but the starting points
    													# should differ by only angle pi/5
    prev_x = 100*cos(theta) + 250
    prev_y = 100*sin(theta) + 250
    
    for i in range(20):
    	glBegin(GL_LINES)
    	theta = theta + (4*pi/5)
    	new_x = 100*cos(theta) + 250
    	new_y = 100*sin(theta) + 250
    	
    	glVertex2f(prev_x, prev_y)
    	glVertex2f(new_x, new_y)
    	prev_x = new_x
    	prev_y = new_y
    	glEnd()
    	   	
   	
    glutSwapBuffers()                                  # important for double buffering
   

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Q2_IIT2020504")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()  
