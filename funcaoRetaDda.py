from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 300
window_width = 300
window_title = b"Renderizar ponto com OpenGL"

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, window_width, 0, window_height)  


def funcao_reta_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1

    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)  
    for _ in range(int(steps) + 1):  
        glVertex2f(x, y)
        x += x_inc
        y += y_inc
    glEnd()
    glFlush()


def render():
    """Função de renderização."""
    glClear(GL_COLOR_BUFFER_BIT)
    funcao_reta_dda(50, 50, 250, 250)  


def main():
    """Função principal."""
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(window_title)
    init()
    glutDisplayFunc(render)
    glutMainLoop()


if __name__ == "__main__":
    main()
