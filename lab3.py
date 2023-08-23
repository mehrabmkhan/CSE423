from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def circlePoints(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)

def midpointLine(radius, x0, y0):
    d = 1 - radius
    x = 0
    y = radius

    circlePoints(x, y, x0, y0)

    while x < y:
        #print(y)
        if d < 0:
            # Choose East.
            d = d + 2*x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2*x -2*y + 5
            x += 1
            y = y - 1

        circlePoints(x, y, x0, y0)

def draw_circle(radius, x0, y0):
    midpointLine(radius, x0, y0)        # outer circle

    #midpointLine(radius/2, x0+radius/2, y0) # Left inner circle
    midpointLine(radius / 2, x0 - radius / 2, y0)  # right inner circle
    midpointLine(radius / 2, x0, y0 + radius/2)  # upper inner circle
    midpointLine(radius / 2, x0, y0 - radius/2)  # Lower inner circle

    #  radius/2.

    opposite = math.sin(math.radians(45)) * radius/2


    midpointLine(radius/2, x0+opposite, y0+opposite)       # Right upper
    midpointLine(radius/2, x0+opposite, y0-opposite)      # Right lower
    midpointLine(radius/2, x0-opposite, y0+opposite)     # Left upper
    midpointLine(radius/2, x0-opposite, y0-opposite)    # Left LOWER

def draw_points(x, y):
    glPointSize(2)

    glBegin(GL_POINTS)

    glVertex2f(x, y)

    glEnd()



def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()


    glColor3f(1.0, 0.0, 0.0)


    draw_circle(200, 600, 300)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)


glutInitWindowSize(1200, 1200)

glutInitWindowPosition(0, 0)


wind = glutCreateWindow(b"LAB03_19101378")

glutDisplayFunc(showScreen)
glutMainLoop()