# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/importOri.ui'
#
# Created: Tue Apr 20 11:40:08 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_importORI(object):
    def setupUi(self, importORI):
        importORI.setObjectName("importORI")
        importORI.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(importORI)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtGui.QWidget(importORI)
        self.widget.setGeometry(QtCore.QRect(10, 0, 318, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_section = QtGui.QLabel(self.widget)
        self.label_section.setObjectName("label_section")
        self.horizontalLayout.addWidget(self.label_section)
        self.lineSectionOri = QtGui.QLineEdit(self.widget)
        self.lineSectionOri.setObjectName("lineSectionOri")
        self.horizontalLayout.addWidget(self.lineSectionOri)
        self.buttonSectionOri = QtGui.QPushButton(self.widget)
        self.buttonSectionOri.setObjectName("buttonSectionOri")
        self.horizontalLayout.addWidget(self.buttonSectionOri)
        self.widget1 = QtGui.QWidget(importORI)
        self.widget1.setGeometry(QtCore.QRect(10, 40, 311, 27))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_points = QtGui.QLabel(self.widget1)
        self.label_points.setObjectName("label_points")
        self.horizontalLayout_2.addWidget(self.label_points)
        self.linePointsOri = QtGui.QLineEdit(self.widget1)
        self.linePointsOri.setObjectName("linePointsOri")
        self.horizontalLayout_2.addWidget(self.linePointsOri)
        self.buttonPointsOri = QtGui.QPushButton(self.widget1)
        self.buttonPointsOri.setObjectName("buttonPointsOri")
        self.horizontalLayout_2.addWidget(self.buttonPointsOri)
        self.label_section.setBuddy(self.lineSectionOri)
        self.label_points.setBuddy(self.linePointsOri)

        self.retranslateUi(importORI)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), importORI.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), importORI.reject)
        QtCore.QMetaObject.connectSlotsByName(importORI)

    def retranslateUi(self, importORI):
        importORI.setWindowTitle(QtGui.QApplication.translate("importORI", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_section.setText(QtGui.QApplication.translate("importORI", "Select section.ori file:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSectionOri.setText(QtGui.QApplication.translate("importORI", "load", None, QtGui.QApplication.UnicodeUTF8))
        self.label_points.setText(QtGui.QApplication.translate("importORI", "Select points.ori file:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonPointsOri.setText(QtGui.QApplication.translate("importORI", "load", None, QtGui.QApplication.UnicodeUTF8))

