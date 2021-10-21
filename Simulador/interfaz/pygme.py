import pygame
from pygame.locals import *

#Esto lo debe retornar el programa principal
def cargar():
    dir = "C:/Users/Juan Camilo/Desktop/prueba/Mapa1.txt"
    file = open(dir,"r")
    mapa = []
    for i in file:
        fila = []
        for j in i:
            j = j.strip("\n")
            if j!="": fila.append(j)
        mapa.append(fila)
    return mapa

def leerDatos(mapa):
    coords = []
    for i in range(len(mapa)):
        st = False
        for j in range(len(mapa[i])-1,0,-1):
            if (mapa[i][j] == "-" or mapa[i][j] == "|") and st == False:
                st = True
                coords.append([(i, j), (0, 0)])
            if st and mapa[i][j] == " ":
                st = False
                coords[len(coords)-1][1] = tuple([i,j-1])
    return coords

RED = (255,0,0)

ALTO = 600
ANCHO = 600
xmax = 64
xmin = -64
ymax = 64
ymin = -64

def punto(p):
    return [p[0]*(ANCHO/(xmax-xmin))+ANCHO/2,p[1]*ALTO/(ymax-ymin)+ALTO/2]
def linea(coords,c):
    for i in coords:
        pygame.draw.line(screen, c, punto([i[0][0], i[0][1]]), punto([i[1][0], i[1][1]]), 2)

pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("Simulador")
fin = False

while not fin:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            fin = True
    screen.fill((255,255,255))

    linea(leerDatos(cargar()), RED)


    pygame.display.update()
