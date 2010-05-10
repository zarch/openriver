# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon May 10 13:23:57 2010
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
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.listSections = QtGui.QListWidget(self.splitter)
        self.listSections.setObjectName("listSections")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineTabEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineTabEdit.setObjectName("lineTabEdit")
        self.verticalLayout.addWidget(self.lineTabEdit)
        self.tableSectionCoord = QtGui.QTableView(self.layoutWidget)
        self.tableSectionCoord.setObjectName("tableSectionCoord")
        self.verticalLayout.addWidget(self.tableSectionCoord)
        self.verticalLayout_2.addWidget(self.splitter)
        self.sectionGraphics = QtGui.QGraphicsView(self.centralwidget)
        self.sectionGraphics.setObjectName("sectionGraphics")
        self.verticalLayout_2.addWidget(self.sectionGraphics)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 24))
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
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionView = QtGui.QAction(MainWindow)
        self.actionView.setObjectName("actionView")
        self.menu_File.addAction(self.actionImport)
        self.menu_File.addAction(self.actionExport)
        self.menu_File.addAction(self.action_Open)
        self.menuSimulation.addAction(self.actionRun)
        self.menuSimulation.addAction(self.actionView)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuSimulation.menuAction())
        self.toolBar.addAction(self.actionRun)

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
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("MainWindow", "&Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView.setText(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))

