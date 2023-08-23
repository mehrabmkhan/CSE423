from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# This function is used to draw lines.
def draw_lines():
    glBegin(GL_LINES)
#===========1===========#
    glColor3f(1.0, 0.0, 0.0)    # Colour = Red
    glVertex2f(-200, 350)
    glVertex2f(-200, 50)


    print("1")

#===========9===========#
    glColor3f(0.0, 1.0, 0.0)  # Colour = Green
    glVertex2f(-150, 350)
    glVertex2f(-100, 350)
    glVertex2f(-100, 350)
    glVertex2f(-100, 200)
    glVertex2f(-100, 200)
    glVertex2f(-150, 200)
    glVertex2f(-150, 200)
    glVertex2f(-150, 350)
    glVertex2f(-100, 200)
    glVertex2f(-100, 50)
    glVertex2f(-100, 50)
    glVertex2f(-150, 50)

    print("9")

#===========1===========#
    glColor3f(0.0, 0.0, 1.0)  # Colour = Blue
    glVertex2f(-20, 50)
    glVertex2f(-20, 350)

    print("1")

#===========0===========#
    glVertex2f(30, 50)
    glVertex2f(80, 50)
    glVertex2f(80, 50)
    glVertex2f(80, 350)
    glVertex2f(80, 350)
    glVertex2f(30, 350)
    glVertex2f(30, 350)
    glVertex2f(30, 50)

    print("0")

#===========1===========#
    glVertex2f(160, 50)
    glVertex2f(160, 350)

    print("1")

#===========3===========#
    glColor3f(1.0, 1.0, 1.0)  # Colour = White
    glVertex2f(200, 350)
    glVertex2f(300, 350)
    glVertex2f(300, 350)
    glVertex2f(300, 50)
    glVertex2f(300, 50)
    glVertex2f(200, 50)
    glVertex2f(300, 200)
    glVertex2f(200, 200)

    print("3")

#===========7===========#
    glColor3f(1.0, 0.0, 1.0)  # Colour = Purple
    glVertex2f(350, -350)
    glVertex2f(300, 350)
    glVertex2f(300, 350)
    glVertex2f(300, 50)
    glVertex2f(300, 50)

    print("7")

#===========8===========#
        # Colour = Rainbow
    # --------vertical_lines--------#
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(400, 50)
    glVertex2f(450, 50)
    glVertex2f(450, 50)
    glVertex2f(450, 200)
    glVertex2f(450, 200)
    glVertex2f(400, 200)
    glVertex2f(400, 200)
    glVertex2f(400, 50)
    glVertex2f(400, 350)
    glVertex2f(450, 350)

    print("8")

    glEnd()


def iterate():
    glViewport(0, 0, 900, 400)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 900, 0.0, 400, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # (Red, Green, Blue)
    #glColor3f(1.0, 1.0, 0.0)

    ###============================###
    ### call_the_draw_methods_here ###
    ###============================###
    # draw_lines function to draw lines.
    draw_lines()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

# Size of the window.
# Manipulating this value will let us change the size of the output widow.
glutInitWindowSize(900, 400)
glutInitWindowPosition(0, 0)

# window name
wind = glutCreateWindow(b"Task03: Student ID")

glutDisplayFunc(showScreen)

glutMainLoop()