from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def findZone(x0, y0, x1, y1):

    dy = y1-y0
    dx = x1-x0

    if abs(dx) > abs(dy):   # Represents zone 0, 3, 4, 7.
        if dx > 0 and dy > 0:
            print("FindZone: 0")
            return 0
        elif dx < 0 and dy > 0:
            print("FindZone: 3")
            return 3
        elif dx < 0 and dy < 0:
            print("FindZone: 4")
            return 4
        else:
            print("FindZone: 7")
            return 7

    else:                   # Represents zone 1, 2, 5, 6.
        if dx > 0 and dy > 0:
            print("FindZone: 1")
            return 1
        elif dx < 0 and dy > 0:
            print("FindZone: 2")
            return 2
        elif dx < 0 and dy < 0:
            print("FindZone: 5")
            return 5
        else:
            print("FindZone: 6")
            return 6



def ZoneZeroConversion(zone, x, y):

    if zone == 0:
        print("Zone Zero Conversion Executed:", x, ",", y)
        return x, y
    elif zone == 1:
        print("Zone Zero Conversion Executed:", y, ",", x)
        return y, x
    elif zone == 2:
        print("Zone Zero Conversion Executed:", -y, ",", x)
        return -y, x
    elif zone == 3:
        print("Zone Zero Conversion Executed:", -x, ",", y)
        return -x, y
    elif zone == 4:
        print("Zone Zero Conversion Executed:", -x, ",", -y)
        return -x, -y
    elif zone == 5:
        print("Zone Zero Conversion Executed:", -y, ",", -x)
        return -y, -x
    elif zone == 6:
        print("Zone Zero Conversion Executed:", -y, ",", x)
        return -y, x
    elif zone == 7:
        print("Zone Zero Conversion Executed:", x, ",", -y)
        return x, -y

def zero_to_original_zone(zone, x, y):

    if zone == 0:
        print("Converted to original zone:", x, ",", y)
        return x, y
    if zone == 1:
        print("Converted to original zone:", y, ",", x)
        return y, x
    if zone == 2:
        print("Converted to original zone:", -y, ",", -x)
        return -y, -x
    if zone == 3:
        print("Converted to original zone:", -x, ",", y)
        return -x, y
    if zone == 4:
        print("Converted to original zone:", -x, ",", -y)
        return -x, -y
    if zone == 5:
        print("Converted to original zone:", -y, ",", -x)
        return -y, -x
    if zone == 6:
        print("Converted to original zone:", y, ",", -x)
        return y, -x
    if zone == 7:
        print("Converted to original zone:", x, ",", -y)
        return x, -y
def MidPointLine(zone, x0, y0, x1, y1):

    dy = y1-y0
    dx = x1-x0
    d_init = 2*dy - dx
    e = 2*dy
    ne = 2*(dy-dx)

    x = x0
    y = y0

    while x <= x1:

        a, b = zero_to_original_zone(zone, x, y)        # The process involves converting the points back to the original zone and then drawing them.





        draw_points(a, b)
        print("point drawn")

        if d_init <= 0:
            x += 1
            d_init += e

        else:
            x += 1
            y += 1
            d_init += ne

def eight_way_symmetry(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    z0_x0, z0_y0 = ZoneZeroConversion(zone, x0, y0)
    z0_x1, z0_y1 = ZoneZeroConversion(zone, x1, y1)
    MidPointLine(zone, z0_x0, z0_y0, z0_x1, z0_y1)
    print("Task done!")
    print("=================================================================")
    print()

def seven():
    eight_way_symmetry(100, 400, 200, 400)
    eight_way_symmetry(100, 200, 200, 400)


def eight():

    eight_way_symmetry(300, 400, 400, 400)
    eight_way_symmetry(300, 300, 400, 300)
    eight_way_symmetry(300, 200, 400, 200)
    eight_way_symmetry(400, 400, 400, 200)
    eight_way_symmetry(300, 400, 300, 200)

def draw_points(x, y):
    # The size of the pixel is determined by the parameter passed into the function.
    glPointSize(9)

    glBegin(GL_POINTS)

    # Consider this as a coordinate. The pixel will be drawn at the specified x and y position.
    glVertex2f(x, y)


    glEnd()

def iterate():
    glViewport(0, 0, 500, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # (Red, Green, Blue)
    glColor3f(2.3, 3.0, 1.0)


    seven()
    eight()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)


glutInitWindowSize(500, 600)

glutInitWindowPosition(0, 0)


wind = glutCreateWindow(b"lab02: midpoint Line Drawing")

glutDisplayFunc(showScreen)

glutMainLoop()