# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewSimulation2.ui'
#
# Created: Tue May 11 17:07:01 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 538)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GraphicSimulation1D = QtGui.QGraphicsView(self.centralwidget)
        self.GraphicSimulation1D.setGeometry(QtCore.QRect(9, 103, 711, 331))
        self.GraphicSimulation1D.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemShape)
        self.GraphicSimulation1D.setObjectName("GraphicSimulation1D")
        self.listProfiles = QtGui.QListWidget(self.centralwidget)
        self.listProfiles.setEnabled(True)
        self.listProfiles.setGeometry(QtCore.QRect(10, 40, 701, 51))
        self.listProfiles.setObjectName("listProfiles")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 281, 18))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 24))
        self.menubar.setObjectName("menubar")
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
        self.actionView.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionView.setObjectName("actionView")

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.listProfiles, QtCore.SIGNAL("currentRowChanged(int)"), MainWindow.itemChanged)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation Results", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Select a time step (time in seconds):", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("MainWindow", "&Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView.setText(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))

