from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 300
window_width = 300
window_title = b"Renderizar reta analitica com OpenGL"

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, window_width, 0, window_height)  

def reta_analitica(m, b, x_start, x_end):
    x = x_start
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0) 
    
    while x <= x_end:
        y = m * x + b  
        glVertex2f(x, y)
        x += 1  

    glEnd()
    glFlush()

def render():
    """Função de renderização."""
    glClear(GL_COLOR_BUFFER_BIT)
    m = 0.5  
    b = 50   
    x_start = 0  
    x_end = 300  
    reta_analitica(m, b, x_start, x_end)  

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
