# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1264, 1101)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(600, 0, 661, 1061))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 210, 601, 491))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_OpenGL = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_OpenGL.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_OpenGL.setObjectName("gridLayout_OpenGL")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1264, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.New_menu = QtWidgets.QAction(MainWindow)
        self.New_menu.setObjectName("New_menu")
        self.Open_menu = QtWidgets.QAction(MainWindow)
        self.Open_menu.setObjectName("Open_menu")
        self.Exit_menu = QtWidgets.QAction(MainWindow)
        self.Exit_menu.setObjectName("Exit_menu")
        self.SPL_menu = QtWidgets.QAction(MainWindow)
        self.SPL_menu.setObjectName("SPL_menu")
        self.RT60_menu = QtWidgets.QAction(MainWindow)
        self.RT60_menu.setObjectName("RT60_menu")
        self.menuFile.addAction(self.New_menu)
        self.menuFile.addAction(self.Open_menu)
        self.menuFile.addAction(self.Exit_menu)
        self.menuTools.addAction(self.RT60_menu)
        self.menuTools.addAction(self.SPL_menu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.New_menu.setText(_translate("MainWindow", "NEW"))
        self.Open_menu.setText(_translate("MainWindow", "Open"))
        self.Exit_menu.setText(_translate("MainWindow", "EXIT"))
        self.SPL_menu.setText(_translate("MainWindow", "SPL CALCULATOR"))
        self.RT60_menu.setText(_translate("MainWindow", "RT 60 CALCULATOR"))

