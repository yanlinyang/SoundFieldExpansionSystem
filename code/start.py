from mainWindow import Ui_MainWindow
from yly import MyOpenGLWindow
from Object import ObjectModel
import pygame
from PyQt5.QtCore import QTimer

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,math
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

from PyQt5.QtWidgets import QFileDialog

import glfw
from OpenGL.GL import *
import ShaderLoader
# import numpy
# import pyrr
# from PIL import Image
# from ObjLoader import *


from Rt60Page import Ui_Rt60Page
from SplPage import Ui_SplPage


def window_resize(window, width, height):
    glViewport(0, 0, width, height)

class UIshow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(UIshow, self).__init__()
        self.setupUi(self)

        self.openGLWidget = MyOpenGLWindow(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(0, 40, 500, 500))
        self.openGLWidget.setObjectName("openGLWidget")
        self.gridLayout_OpenGL.addWidget(self.openGLWidget)
        self.rt60_c = Rt60_Page()
        self.spl_c = Spl_Page()

        self.Open_menu.triggered.connect(self.openFile)

        self.RT60_menu.triggered.connect(self.openRT60Page)
        self.SPL_menu.triggered.connect(self.openSplPage)

    def basic(self):
        # 设置标题，大小，图标
        self.setWindowTitle("GT")
        self.resize(500, 50)
        # self.setWindowIcon(QIcon("./image/Gt.png"))
        # 居中显示
        screen = MyOpenGLWindow().geometry()
        self_size = self.geometry()
        self.move((screen.width() - self_size.width()) / 2, (screen.height() - self_size.height()) / 2)


    def CloseOtherWidgets(self):
        self.rt60_c.close()
        self.spl_c.close()





    def openFile(self):
        openfile_name, fileFormat = QFileDialog.getOpenFileName(self, '选择3D文件', '', 'wav files(*.obj)')
        self.loadFile(openfile_name)

    def loadFile(self,openfile_name):
        pass

    def openRT60Page(self):
        self.CloseOtherWidgets()
        self.rt60_c.openGLArea = self.openGLWidget
        self.gridLayout.addWidget(self.rt60_c)
        self.rt60_c.show()


    def openSplPage(self):
        self.CloseOtherWidgets()
        self.spl_c.openGLArea = self.openGLWidget
        self.gridLayout.addWidget(self.spl_c)
        self.spl_c.show()


class Rt60_Page(QtWidgets.QMainWindow, Ui_Rt60Page):
    def __init__(self):
        super(Rt60_Page, self).__init__()
        self.setupUi(self)
        self.openGLArea = None
        self.calculateRT60.clicked.connect(self.calculate_RT60)
        self.displaRoomModel.clicked.connect(self.openGLTest)

    def openGLTest(self):
        # self.openGLArea.setGeometry(QtCore.QRect(0, 40, 500, 500))
        # self.openGLArea.myDraw()
        room_length = float(self.room_length.text())
        room_width = float(self.room_width.text())
        room_height = float(self.room_height.text())
        self.openGLArea.setSize(room_length,room_height,room_width)


    def calculate_RT60(self):
        k = 0.161
        # 大理石 混凝土  砖块(粗糙)  木板
        Sa_set = [[0.01,0.01,0.01,0.02,0.02,0.024],[0.01,0.01,0.02,0.02,0.02,0.03],[0.36,0.44,0.31,0.29,0.39,0.25],[0.05,0.06,0.06,0.1,0.1,0.1]]

        room_length = float(self.room_length.text())
        room_width = float(self.room_width.text())
        room_height = float(self.room_height.text())
        material_selection = self.material_selection.currentIndex()
        # frequency_selection = self.buttonGroup1.checkedId()
        print(room_length, room_width, room_height, self.material_selection.currentText())

        rt_60 = []
        for i in range(len(Sa_set[0])):
            Sa = (2*room_length*room_width+ 2*room_length*room_height+2*room_width*room_height) * Sa_set[int(material_selection)][i]
            print(Sa)

            rt_60_ = k*(room_length*room_width*room_height/Sa)
            rt_60.append(rt_60_)
        print(rt_60)
        # self.rt60_value.setText(str(round(rt_60,2)))

        dr = Figure_Canvas(range(6), rt_60, title="RT 60", xlabel="Frequency(Hz)", ylabel="RT 60(s)")
        # 实例化一个FigureCanvas

        # dr.plot(wavetime,wave_data[0],"ti")  # 画图
        graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.rt60_graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.rt60_graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!
        # 线程
        # thread = Thread(target=task, args=(self.p, self.playPage_FileAddressEdit.text(),))
        # thread.start()

        print("end")


class Spl_Page(QtWidgets.QMainWindow, Ui_SplPage):
    def __init__(self):
        super(Spl_Page, self).__init__()
        self.setupUi(self)
        self.openGLArea = None
        self.buttonGroup1 = QtWidgets.QButtonGroup(self)
        self.buttonGroup1.addButton(self.radioButton_1, 0)
        self.buttonGroup1.addButton(self.radioButton_2, 1)
        self.buttonGroup1.addButton(self.radioButton_3, 2)

        self.calculateSPL.clicked.connect(self.calculate_SPL)

    def calculate_SPL(self):
        speakerSensitivity = float(self.SpeakerSensitivity.text())
        amplifierPower = float(self.AmplifierPower.text())
        distance = float(self.Distance.text())
        no_of_Speakers = int(self.No_of_Speakers.text())
        speakerPlacement = self.buttonGroup1.checkedId()

        powerdb = 10*math.log(amplifierPower,10)
        distancedb = -20 * math.log(distance, 10)
        qty = 10 * (math.log(no_of_Speakers*amplifierPower,10)-math.log(amplifierPower,10))
        placement = speakerPlacement * 3
        totaldb = speakerSensitivity + powerdb + distancedb + qty + placement

        print(powerdb,distancedb,qty,placement,totaldb)

        # speakerMaxSPL = speakerSensitivity + 10 * math.log(amplifierPower,10)
        # spl = speakerMaxSPL - 20 * math.log(distance,10)
        self.spl_result_text.setText(str(totaldb))

        x = np.linspace(0, self.openGLArea.room_length, 100)
        y = np.linspace(0, self.openGLArea.room_width, 100)
        X, Y = np.meshgrid(x, y)
        if speakerPlacement==1:
            speakerPoint = [self.openGLArea.room_length-1, self.openGLArea.room_width/2]
        elif speakerPlacement==2:
            speakerPoint = [self.openGLArea.room_length*0.9, self.openGLArea.room_width*0.9]
        else:
            speakerPoint = [self.openGLArea.room_length/2, self.openGLArea.room_width/2]


        print(speakerPoint)

        dist = np.sqrt((X-speakerPoint[0])*(X-speakerPoint[0])+(Y-speakerPoint[1])*(Y-speakerPoint[1]))
        spl_all = -20 * np.log10(dist)
        print(spl_all)
        spl_all += speakerSensitivity + powerdb + qty + placement
        print(spl_all)
        dr = Figure_Canvas_spl_2d(X,Y,spl_all,speakerPoint)
        # 实例化一个FigureCanvas

        # dr.plot(wavetime,wave_data[0],"ti")  # 画图
        graphicscene_2d = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene_2d.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.spl_graphicsView_2d.setScene(graphicscene_2d)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.spl_graphicsView_2d.show()

        dr = Figure_Canvas_spl_3d(X, Y, spl_all, speakerPoint)
        # 实例化一个FigureCanvas

        # dr.plot(wavetime,wave_data[0],"ti")  # 画图
        graphicscene_3d = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene_3d.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.spl_graphicsView_3d.setScene(graphicscene_3d)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.spl_graphicsView_3d.show()


class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键

    def __init__(self, x,y,parent=None, width=8, height=5, dpi=10,title="",xlabel="",ylabel=""):
        fig = Figure(figsize=(width, height), dpi=55)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig) # 初始化父类
        self.setParent(parent)
        fig.tight_layout()
        font1 = {'fontsize': 18,
                 'fontweight': 'normal',
                 }
        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

        # self.axes.set_title(title,fontdict=font1)
        self.axes.set_xlabel(xlabel,fontdict=font1)
        self.axes.set_ylabel(ylabel, fontdict=font1)

        group_xlabels = ['0','125', '250', '500', '1k', '2k', '4k']
        group_ylabels = [str(i) for i in range(int(max(y))+2)]
        # self.axes.set_xlim(0, 6)
        self.axes.set_xticklabels(group_xlabels,rotation=0,fontdict=font1)
        self.axes.set_ylim(0,max(y)+1)
        # self.axes.set_yticklabels(group_ylabels,rotation=0,fontdict=font1)
        self.axes.plot(y,'b-o')
        for i in range(len(x)):
            self.axes.plot([x[i],x[i]],[y[i],0],'g')
        for x, y in zip(x, y):
            self.axes.text(x+0.1, y + 0.05, str(round(y,2)), ha='center', va='bottom', fontsize=16, color='g')
        fig.subplots_adjust(left=0.08, top=1, right=0.95, bottom=0.15, wspace=0, hspace=0)

class Figure_Canvas_spl_3d(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键

    def __init__(self, X,Y,dist, speakerPoint,width=10, height=6):
        font1 = {'fontsize': 18,
                 'fontweight': 'normal',
                 }
        fig = Figure(figsize=(width, height), dpi=55)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig) # 初始化父类
        # fig.tight_layout()
        font1 = {'fontsize': 18,
                 'fontweight': 'normal',
                 }

        self.axes = fig.add_subplot(111, projection='3d')

        self.axes.set_xlabel("length", fontdict=font1)
        self.axes.set_ylabel("width", fontdict=font1)
        self.axes.set_zlabel("spl(db)", fontdict=font1)

        surf = self.axes.plot_surface(X, Y, dist, rstride=1, cstride=1, cmap=cm.viridis,
                               linewidth=0, antialiased=False)
        # self.axes.set_zlim3d(-1.01, 1.01)
        fig.colorbar(surf, shrink=0.5, aspect=5)
        # fig.subplots_adjust(left=0.08, top=0.95, right=1, bottom=0.15, wspace=0, hspace=0)
        fig.tight_layout(pad=-3,h_pad=-1)


class Figure_Canvas_spl_2d(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键

    def __init__(self, X,Y, dist, speakerPoint,width=10, height=6):
        font1 = {'fontsize': 18,
                 'fontweight': 'normal',
                 }
        fig = Figure(figsize=(width, height), dpi=55)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig) # 初始化父类
        # fig.tight_layout()
        font1 = {'fontsize': 18,
                 'fontweight': 'normal',
                 }

        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

        self.axes.set_xlabel("length", fontdict=font1)
        self.axes.set_ylabel("width", fontdict=font1)

        surf = self.axes.contourf(X, Y, dist,extend='both')
        self.axes.plot(speakerPoint[0], speakerPoint[1], 'o')
        fig.colorbar(surf, shrink=0.5, aspect=5)
        fig.subplots_adjust(left=0.08, top=0.95, right=0.95, bottom=0.15, wspace=0, hspace=0)

        '''
        self.axes = fig.add_subplot(111, projection='3d')
        surf = self.axes.plot_surface(X, Y, dist, rstride=1, cstride=1, cmap=cm.viridis,
                               linewidth=0, antialiased=False)
        # self.axes.set_zlim3d(-1.01, 1.01)
        fig.colorbar(surf, shrink=0.5, aspect=5)
        # fig.subplots_adjust(left=0.08, top=0.95, right=1, bottom=0.15, wspace=0, hspace=0)
        fig.tight_layout(pad=-5,h_pad=-5)
        '''


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = UIshow()
    window.show()
    sys.exit(app.exec_())