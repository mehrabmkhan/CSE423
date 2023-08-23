from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500

def draw_line(x1, y1, x2, y2):
    # Calculate the differences in x and y
    dx = x2 - x1
    dy = y2 - y1

    # Initialize the decision parameter
    d = dy - (dx/2)
    x = x1
    y = y1

    # Start drawing points
    glBegin(GL_POINTS)
    while x <= x2:
        glVertex2i(int(x), int(y))
        x += 1
        if d < 0:
            d = d + dy
        else:
            d = d + dy - dx
            y += 1
    glEnd()

def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)

    glColor3f(0.0, 0.0, 1.0) # Set color to blue

    # Draw the number '78'
    # Draw '7'
    draw_line(10, 80, 70, 80)
    draw_line(70, 80, 40, 10)
    # Draw '8'
    draw_line(100, 10, 100, 80)
    draw_line(100, 80, 140, 80)
    draw_line(140, 80, 140, 10)
    draw_line(140, 10, 100, 10)

    glutSwapBuffers() # Swaps the buffers of the current window if double buffered

glutInit() # Initialize a glut instance which will allow us to customize our window
glutInitDisplayMode(GLUT_RGB) # Set the display mode to be colored
glutInitWindowSize(width, height) # Set the width and height of your window
glutInitWindowPosition(0, 0) # Set the position at which this windows should appear
wind = glutCreateWindow("OpenGL Coding Practice") # Give your window a title
glutDisplayFunc(show_screen) # Tell OpenGL to call the showScreen method continuously
glutIdleFunc(show_screen) # Draw any graphics or shapes in the showScreen function at all times
gluOrtho2D(0, width, 0, height) # Set the width and height of your window
glutMainLoop()  # Keeps the window created above displaying/running in a loop
