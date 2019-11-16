from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtOpenGL import *
from OpenGL.GLUT import *
import numpy as np
import math

# def mousePressEvent(button, state, x, y):
#     print(1)

class MyOpenGLWindow(QtWidgets.QOpenGLWidget):
    def __init__(self, parent):
        QtWidgets.QOpenGLWidget.__init__(self, parent)
        self.setMinimumSize(200, 200)
        # self.room_length = 1
        # self.room_width = 1
        # self.room_height = 1
        # self.room_size = np.array([self.room_length,self.room_height,self.room_width]) /(self.room_length+self.room_height+self.room_width)

        # glClearColor(0.0, 0.0, 0.0, 1.0)  # 设置画布背景色。注意：这里必须是4个参数
        # glEnable(GL_DEPTH_TEST)  # 开启深度测试，实现遮挡关系
        # glDepthFunc(GL_LEQUAL)


    def initializeGL(self):
        self.room_length = 1
        self.room_width = 1
        self.room_height = 1

        glRotate(15, -1, 1, 0)
        # glClearColor(0, 0, 0, 1)
        # glEnable(GL_DEPTH_TEST)
        # glEnable(GL_LIGHT0)
        # glEnable(GL_LIGHTING)
        # glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        # glEnable(GL_COLOR_MATERIAL)


    def paintGL(self):
        self.room_size = np.array([self.room_length, self.room_height, self.room_width]) / (
                    self.room_length + self.room_height + self.room_width)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        glLineStipple(5, 0x5555)
        glEnable(GL_LINE_STIPPLE)

        glBegin(GL_LINES)
        # 以红色绘制x轴
        glColor4f(1.0, 0.0, 0.0, 1.0)  # 设置当前颜色为红色不透明
        glVertex3f(-0.8, 0.0, 0.0)  # 设置x轴顶点（x轴负方向）
        glVertex3f(0.8, 0.0, 0.0)  # 设置x轴顶点（x轴正方向）

        # 以绿色绘制y轴
        glColor4f(0.0, 1.0, 0.0, 1.0)  # 设置当前颜色为绿色不透明
        glVertex3f(0.0, -0.8, 0.0)  # 设置y轴顶点（y轴负方向）
        glVertex3f(0.0, 0.8, 0.0)  # 设置y轴顶点（y轴正方向）

        # 以蓝色绘制z轴
        glColor4f(0.0, 0.0, 1.0, 1.0)  # 设置当前颜色为蓝色不透明
        glVertex3f(0.0, 0.0, -0.8)  # 设置z轴顶点（z轴负方向）
        glVertex3f(0.0, 0.0, 0.8)  # 设置z轴顶点（z轴正方向）

        glEnd()
        glLineStipple(5, 0xFFFF)
        glEnable(GL_LINE_STIPPLE)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        print(self.room_size)
        self.objSize = self.room_size
        print(self.objSize)
        verticies = ((self.objSize[0], -self.objSize[1], -self.objSize[2]),
                     (self.objSize[0], self.objSize[1], -self.objSize[2]),
                     (-self.objSize[0], self.objSize[1], -self.objSize[2]),
                     (-self.objSize[0], -self.objSize[1], -self.objSize[2]),
                     (self.objSize[0], -self.objSize[1], self.objSize[2]),
                     (self.objSize[0], self.objSize[1], self.objSize[2]),
                     (-self.objSize[0], -self.objSize[1], self.objSize[2]),
                     (-self.objSize[0], self.objSize[1], self.objSize[2]),
                     (6 / 4 * self.objSize[0], -4 / 4 * self.objSize[1], -3 / 4 * self.objSize[2]),
                     (6 / 4 * self.objSize[0], 3 / 4 * self.objSize[1], -3 / 4 * self.objSize[2]),
                     (6 / 4 * self.objSize[0], -4 / 4 * self.objSize[1], 3 / 4 * self.objSize[2]),
                     (6 / 4 * self.objSize[0], 3 / 4 * self.objSize[1], 3 / 4 * self.objSize[2])
                     )

        edges = ((0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7),
                 (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7),
                 (0,8),(1,9),(4,10),(5,11), (8,9),(9,11),(11,10),(10,8)
                 )
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(verticies[vertex])
        glEnd()
        glRotatef(15, 0, 0.5, 0)

        # glutMouseFunc(mousePressEvent)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下
            glRotatef(50, 0, 1, 0)
            # glScalef(1.5, 1.5, 1.5)
            self.update()

    def wheelEvent(self, event):
        angle = event.angleDelta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
        print(angle)
        angleX = angle.x()  # 水平滚过的距离(此处用不上)
        angleY = angle.y()  # 竖直滚过的距离
        if angleY > 0:
            glScalef(1.1, 1.1, 1.1)
        else:  # 滚轮下滚
            glScalef(0.9, 0.9, 0.9)
        self.update()

    def setSize(self,x,y,z):
        print("okok")
        self.room_length = x
        self.room_height = y
        self.room_width = z
        self.update()




