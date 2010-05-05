# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewSimulation.ui'
#
# Created: Wed May  5 10:54:16 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_viewSimulation1D(object):
    def setupUi(self, viewSimulation1D):
        viewSimulation1D.setObjectName("viewSimulation1D")
        viewSimulation1D.setWindowModality(QtCore.Qt.NonModal)
        viewSimulation1D.resize(627, 315)
        viewSimulation1D.setMouseTracking(False)
        self.GraphicSimulation1D = QtGui.QGraphicsView(viewSimulation1D)
        self.GraphicSimulation1D.setGeometry(QtCore.QRect(10, 20, 611, 281))
        self.GraphicSimulation1D.setFrameShape(QtGui.QFrame.StyledPanel)
        self.GraphicSimulation1D.setFrameShadow(QtGui.QFrame.Plain)
        self.GraphicSimulation1D.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.GraphicSimulation1D.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.GraphicSimulation1D.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        self.GraphicSimulation1D.setTransformationAnchor(QtGui.QGraphicsView.NoAnchor)
        self.GraphicSimulation1D.setViewportUpdateMode(QtGui.QGraphicsView.SmartViewportUpdate)
        self.GraphicSimulation1D.setObjectName("GraphicSimulation1D")

        self.retranslateUi(viewSimulation1D)
        QtCore.QMetaObject.connectSlotsByName(viewSimulation1D)

    def retranslateUi(self, viewSimulation1D):
        viewSimulation1D.setWindowTitle(QtGui.QApplication.translate("viewSimulation1D", "Simulation Results", None, QtGui.QApplication.UnicodeUTF8))

