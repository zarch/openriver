# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewSimulation.ui'
#
# Created: Tue May  4 23:15:13 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_viewSimulation1D(object):
    def setupUi(self, viewSimulation1D):
        viewSimulation1D.setObjectName("viewSimulation1D")
        viewSimulation1D.resize(400, 300)
        self.GraphicSimulation1D = QtGui.QGraphicsView(viewSimulation1D)
        self.GraphicSimulation1D.setGeometry(QtCore.QRect(10, 10, 381, 291))
        self.GraphicSimulation1D.setObjectName("GraphicSimulation1D")

        self.retranslateUi(viewSimulation1D)
        QtCore.QMetaObject.connectSlotsByName(viewSimulation1D)

    def retranslateUi(self, viewSimulation1D):
        viewSimulation1D.setWindowTitle(QtGui.QApplication.translate("viewSimulation1D", "Form", None, QtGui.QApplication.UnicodeUTF8))

