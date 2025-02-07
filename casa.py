from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 300
window_width = 300
window_title = b"Casa com OpenGL"

def init():
    """Inicializa o ambiente OpenGL."""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Cor de fundo (preto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, window_width, 0, window_height)  # Sistema de coordenadas 2D


def funcao_reta_dda(x1, y1, x2, y2):
    """Desenha uma reta usando o algoritmo DDA (pontos)."""
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1

    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    for _ in range(int(steps) + 1):  # Garantir que todos os pontos sejam desenhados
        glVertex2f(x, y)
        x += x_inc
        y += y_inc
    glEnd()
    glFlush()


def render():
    """Função de renderização."""
    glClear(GL_COLOR_BUFFER_BIT)

    # Corpo da casa (quadrado)
    funcao_reta_dda(100, 100, 100, 200)  
    funcao_reta_dda(100, 200, 200, 200)  
    funcao_reta_dda(200, 200, 200, 100)  
    funcao_reta_dda(200, 100, 100, 100)  

    # Telhado (triângulo)
    funcao_reta_dda(100, 200, 150, 250)  
    funcao_reta_dda(150, 250, 200, 200)  
    funcao_reta_dda(100, 200, 200, 200)  

    # Porta
    funcao_reta_dda(130, 100, 130, 150)  
    funcao_reta_dda(130, 150, 180, 150)  
    funcao_reta_dda(180, 150, 180, 100)  
    funcao_reta_dda(130, 100, 180, 100)  

    # Janela esquerda
    funcao_reta_dda(110, 160, 110, 190)  
    funcao_reta_dda(110, 190, 140, 190)  
    funcao_reta_dda(140, 190, 140, 160)  
    funcao_reta_dda(110, 160, 140, 160)  

    # Janela direita
    funcao_reta_dda(160, 160, 160, 190)  
    funcao_reta_dda(160, 190, 190, 190)  
    funcao_reta_dda(190, 190, 190, 160)  
    funcao_reta_dda(160, 160, 190, 160)  

    glFlush()


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
