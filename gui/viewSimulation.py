# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewSimulation.ui'
#
# Created: Sat May  8 11:22:42 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_viewSimulation1D(object):
    def setupUi(self, viewSimulation1D):
        viewSimulation1D.setObjectName("viewSimulation1D")
        viewSimulation1D.resize(653, 313)
        self.centralwidget = QtGui.QWidget(viewSimulation1D)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.GraphicSimulation1D = QtGui.QGraphicsView(self.centralwidget)
        self.GraphicSimulation1D.setObjectName("GraphicSimulation1D")
        self.verticalLayout_2.addWidget(self.GraphicSimulation1D)
        viewSimulation1D.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(viewSimulation1D)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 24))
        self.menubar.setObjectName("menubar")
        viewSimulation1D.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(viewSimulation1D)
        self.statusbar.setObjectName("statusbar")
        viewSimulation1D.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(viewSimulation1D)
        self.toolBar.setObjectName("toolBar")
        viewSimulation1D.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.actionImport = QtGui.QAction(viewSimulation1D)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtGui.QAction(viewSimulation1D)
        self.actionExport.setObjectName("actionExport")
        self.action_Open = QtGui.QAction(viewSimulation1D)
        self.action_Open.setObjectName("action_Open")
        self.actionRun = QtGui.QAction(viewSimulation1D)
        self.actionRun.setObjectName("actionRun")
        self.actionView = QtGui.QAction(viewSimulation1D)
        self.actionView.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionView.setObjectName("actionView")

        self.retranslateUi(viewSimulation1D)
        QtCore.QObject.connect(self.actionView, QtCore.SIGNAL("triggered()"), viewSimulation1D.showNormal)
        QtCore.QMetaObject.connectSlotsByName(viewSimulation1D)

    def retranslateUi(self, viewSimulation1D):
        viewSimulation1D.setWindowTitle(QtGui.QApplication.translate("viewSimulation1D", "Simulation Results", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("viewSimulation1D", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("viewSimulation1D", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("viewSimulation1D", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("viewSimulation1D", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("viewSimulation1D", "&Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView.setText(QtGui.QApplication.translate("viewSimulation1D", "&View", None, QtGui.QApplication.UnicodeUTF8))

