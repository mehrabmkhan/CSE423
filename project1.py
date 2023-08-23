from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global inp
inp = int(input("Number of fishes: "))


def midPointCircle(c_x, c_y, radius):
    d = 1-radius
    x = 0
    y = radius

    while (x <y):
        if (d < 0):
            d = d + (2 * x + 3)
            x += 1
        else:
            d = d + (2 * x - 2 * y + 5)
            x += 1
            y -= 1
        Circlepoint(x, y, c_x, c_y)



def Circlepoint(x, y, c_x, c_y):

    draw(x + c_x, y + c_y)#1
    draw(y + c_x, x + c_y)#0
    draw(y + c_x, -x + c_y)#7
    draw(x + c_x, -y + c_y)#6
    draw(-x + c_x, -y + c_y)#5
    draw(-y + c_x, -x + c_y)#4
    draw(-y + c_x, x + c_y)#3
    draw(-x + c_x, y + c_y)#2

def draw(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-200, 200, -200, 200, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_points(x,y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def findZone(x1, y1, x2, y2):
    dx = (x2-x1)
    dy = (y2-y1)
    zone = None
    if (abs(dx) >= abs(dy)):
        if (dx >= 0 and dy >= 0):
            zone = 0
        if (dx < 0 and dy >= 0):
            zone = 3
        if (dx < 0 and dy < 0):
            zone = 4
        if (dx >= 0 and dy < 0):
            zone = 7


    elif (abs(dy) > abs(dx)):
        if (dx >= 0 and dy >= 0):
            zone = 1
        if (dx < 0 and dy >= 0):
            zone = 2
        if (dx < 0 and dy < 0):
            zone = 5
        if (dx >= 0 and dy < 0):
            zone = 6
    return zone


def convert_zone0(x1, y1, zone):
    if zone == 0:
        pass
    elif zone == 3:
        x1,y1 = -x1,y1
    elif zone == 4:
        x1,y1 = -x1,-y1
    elif zone == 7:
        x1,y1 = x1,-y1
    elif zone == 1:
        x1,y1 = y1,x1
    elif zone == 2:
        x1,y1 = y1,-x1
    elif zone == 5:
        x1,y1 = -y1,-x1
    elif zone == 6:
        x1,y1 = -y1,x1

    return x1, y1


def org_zone(x1, y1, zone):
    if zone == 0:
        pass
    elif zone == 3:
        x1,y1 = -x1,y1
    elif zone == 4:
        x1,y1 = -x1,-y1
    elif zone == 7:
        x1,y1 = x1,-y1
    elif zone == 1:
        x1,y1 = y1,x1
    elif zone == 2:
        x1,y1 = -y1,x1
    elif zone == 5:
        x1,y1 = -y1,-x1
    elif zone == 6:
        x1,y1 = y1,-x1

    return x1, y1



def midPoint(x1, y1, x2, y2):
    zone = findZone(x1, y1, x2, y2)

    draw_points(x1, y1)

    x1, y1 = convert_zone0(x1, y1, zone)
    x2, y2 = convert_zone0(x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d = 2*dy - dx
    d_E = 2*dy
    d_NE = 2*(dy - dx)
    x = x1
    y = y1

    while (x < x2):
        x = x + 1
        if (d < 0):
            d = d + d_E
        else:
            d = d + d_NE
            y = y + 1
        x_new, y_new =org_zone(x, y, zone)
        draw_points(x_new, y_new)

def iterate():

    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-600, 600, -600, 600, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def boat(x,y):
    glColor3f(1, 0.71, 0.76)  # Change the color to pink (RGB values for pink)
    midPoint(x - 225, y, x + 150, y)
    midPoint(x - 175, y - 75, x + 125, y - 75)
    midPoint(x - 225, y, x - 175, y - 75)
    midPoint(x + 150, y, x + 125, y - 75)

    # human
    midPointCircle(x, y + 140, 40)
    midPoint(x, y + 120, x + 40, y)
    midPoint(x + 40, y, x + 80, y + 100)
    midPoint(x + 80, y + 100, x + 120, y + 80)

    midPoint(x + 120, y + 80, x + 120, y - 1100)

    midPoint(x, y, x + 20, y + 40)
    midPoint(x + 20, y + 40, x + 40, y)

    # water
    for i in range(0, 600, 40):
        water(-i)
        fish(400 - i * 2, -58)
        fish(420 - i * 2, -220)
        fish(455 - i * 2, -358)
        fish(410 - i * 2, -123)
        fish(430 - i * 2, -281)

    for i in range(0, inp):
        fish(130 - i * 14, -428 - i * 14)

def water(z):
    glColor3f(0.529, 0.808, 0.922)
    x = -2000
    y = z
    for i in range(0, 1000):
        midPoint(x, y, x + 10, y + 10)
        midPoint(x + 10, y + 10, x + 10 + 10, y)
        x = x + 10 + 10

def fish(x,y):
    glColor3f(1, 1, 0)
    midPoint(x-15, y, x-15-15, y+15)
    midPoint(x - 15, y, x - 15 - 15, y - 15)
    midPoint(x - 15 - 15, y - 15, x - 15 - 15, y + 15)
    midPointCircle(x, y, 15)
    midPoint(x + 15, y, x + 5, y)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    boat(20, 120)

    glutSwapBuffers()





glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 3")  # window name
glutDisplayFunc(showScreen)
glutMainLoop()