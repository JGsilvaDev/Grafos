import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Função para desenhar um cubo (representando um ponto no edifício)
def cubo(x, y, z, size=0.1):
    vertices = [
        [x - size, y - size, z - size],
        [x + size, y - size, z - size],
        [x + size, y + size, z - size],
        [x - size, y + size, z - size],
        [x - size, y - size, z + size],
        [x + size, y - size, z + size],
        [x + size, y + size, z + size],
        [x - size, y + size, z + size],
    ]
    
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Função para desenhar a rota
def desenhar_rota(rota):
    for i in range(len(rota) - 1):
        inicio = G.nodes[rota[i]]['pos']
        fim = G.nodes[rota[i + 1]]['pos']
        glBegin(GL_LINES)
        glVertex3fv(inicio)
        glVertex3fv(fim)
        glEnd()

# Inicializando o PyGame e o OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, display[0] / display[1], 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Desenhar nós (cubo em cada ponto)
    for node in G.nodes:
        pos = G.nodes[node]['pos']
        cubo(*pos)
    
    # Desenhar a rota
    desenhar_rota(rota)
    
    pygame.display.flip()
    pygame.time.wait(10)
