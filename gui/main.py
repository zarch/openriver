# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main.ui'
#
# Created: Tue Apr 20 16:14:10 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 597)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableSectionCoordView = QtGui.QTableView(self.centralwidget)
        self.tableSectionCoordView.setGeometry(QtCore.QRect(200, 39, 451, 191))
        self.tableSectionCoordView.setObjectName("tableSectionCoordView")
        self.sectionGraphics = QtGui.QGraphicsView(self.centralwidget)
        self.sectionGraphics.setGeometry(QtCore.QRect(4, 241, 645, 311))
        self.sectionGraphics.setObjectName("sectionGraphics")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 10, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.listSections = QtGui.QListWidget(self.centralwidget)
        self.listSections.setGeometry(QtCore.QRect(4, 9, 192, 221))
        self.listSections.setObjectName("listSections")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuSimulation = QtGui.QMenu(self.menubar)
        self.menuSimulation.setObjectName("menuSimulation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.action_Run = QtGui.QAction(MainWindow)
        self.action_Run.setObjectName("action_Run")
        self.menu_File.addAction(self.actionImport)
        self.menu_File.addAction(self.actionExport)
        self.menuSimulation.addAction(self.action_Run)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuSimulation.menuAction())
        self.toolBar.addAction(self.action_Run)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.listSections, QtCore.SIGNAL("currentRowChanged(int)"), MainWindow.itemChanged)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "openriver", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSimulation.setTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Run.setText(QtGui.QApplication.translate("MainWindow", "&Run", None, QtGui.QApplication.UnicodeUTF8))

