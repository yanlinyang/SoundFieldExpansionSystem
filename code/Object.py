import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class ObjectModel():
    def __init__(self,x,y,z):
        pygame.init()
        self.object_init()
        self.objSize = [x,y,z]

    # pygame initialization
    def object_init(self):
        # pygame.init()
        self.size = self.width, self.height = 800, 600
        # self.objSize = [5, 5, 5]
        self.speed = [2, 2]
        self.black = 0, 0, 0
        self.dis = (800, 600)

        self.screen = pygame.display.set_mode(self.size, DOUBLEBUF | OPENGL)

        gluPerspective(45, (self.width / self.height), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -30)
        glRotatef(200, 1, 0, 0)


    def Cube(self, objSize):
        verticies = (( objSize[0], -objSize[1], -objSize[2]),
                     ( objSize[0],  objSize[1], -objSize[2]),
                     (-objSize[0],  objSize[1], -objSize[2]),
                     (-objSize[0], -objSize[1], -objSize[2]),
                     ( objSize[0], -objSize[1],  objSize[2]),
                     ( objSize[0],  objSize[1],  objSize[2]),
                     (-objSize[0], -objSize[1],  objSize[2]),
                     (-objSize[0],  objSize[1],  objSize[2]))
        edges = ((0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7),
                 (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7))
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(verticies[vertex])
        glEnd()

    # pygame main loop
    def loop(self, window):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.display.quit()
                    done = True
                    break
                    return True

                if done:
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        glTranslatef(-0.5, 0, 0)
                    if event.key == pygame.K_RIGHT:
                        glTranslatef(0.5, 0, 0)

                    if event.key == pygame.K_UP:
                        glTranslatef(0, -0.2, 0)
                    if event.key == pygame.K_DOWN:
                        glTranslatef(0, 0.2, 0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glRotatef(0.8, 0, 1, 0)

                    if event.button == 5:
                        glRotatef(-0.8, 0, 1, 0)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.Cube(self.objSize)
            pygame.display.flip()
            return False

        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.left < 0 or self.ballrect.right > self.width:
            self.speed[0] = -self.speed[0]
        if self.ballrect.top < 0 or self.ballrect.bottom > self.height:
            self.speed[1] = -self.speed[1]
        self.screen.fill(self.black)
        self.screen.blit(self.ball, self.ballrect)

