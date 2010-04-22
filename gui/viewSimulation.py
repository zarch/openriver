# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/viewSimulation.ui'
#
# Created: Thu Apr 22 16:35:39 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_viewSimulation(object):
    def setupUi(self, viewSimulation):
        viewSimulation.setObjectName("viewSimulation")
        viewSimulation.resize(400, 300)
        self.GraphicSimulation1D = QtGui.QGraphicsView(viewSimulation)
        self.GraphicSimulation1D.setGeometry(QtCore.QRect(10, 10, 381, 291))
        self.GraphicSimulation1D.setObjectName("GraphicSimulation1D")

        self.retranslateUi(viewSimulation)
        QtCore.QMetaObject.connectSlotsByName(viewSimulation)

    def retranslateUi(self, viewSimulation):
        viewSimulation.setWindowTitle(QtGui.QApplication.translate("viewSimulation", "Form", None, QtGui.QApplication.UnicodeUTF8))

