from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500,500

def draw_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = dy - (dx/2)
    x = x1
    y = y1

    glBegin(GL_POINTS)
    while x <= x2:
        glVertex2i(x, y)
        x += 1
        if d < 0:
            d = d + dy
        else:
            d = d + dy - dx
            y += 1
    glEnd()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0, 1.0, 1.0)
    draw_line(50, 50, 78, 78)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
gluOrtho2D(0, w, 0, h)
glutMainLoop()
