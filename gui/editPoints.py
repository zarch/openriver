# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/editPoints.ui'
#
# Created: Wed Apr 21 15:27:50 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditSection(object):
    def setupUi(self, EditSection):
        EditSection.setObjectName("EditSection")
        EditSection.resize(453, 300)
        self.widget = QtGui.QWidget(EditSection)
        self.widget.setGeometry(QtCore.QRect(1, 11, 264, 59))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineTabEdit = QtGui.QLineEdit(self.widget)
        self.lineTabEdit.setToolTip("")
        self.lineTabEdit.setStatusTip("")
        self.lineTabEdit.setObjectName("lineTabEdit")
        self.horizontalLayout.addWidget(self.lineTabEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.addRow = QtGui.QPushButton(self.widget)
        self.addRow.setObjectName("addRow")
        self.horizontalLayout_2.addWidget(self.addRow)
        self.rmRow = QtGui.QPushButton(self.widget)
        self.rmRow.setObjectName("rmRow")
        self.horizontalLayout_2.addWidget(self.rmRow)
        self.upRow = QtGui.QPushButton(self.widget)
        self.upRow.setObjectName("upRow")
        self.horizontalLayout_2.addWidget(self.upRow)
        self.downRow = QtGui.QPushButton(self.widget)
        self.downRow.setObjectName("downRow")
        self.horizontalLayout_2.addWidget(self.downRow)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label.setBuddy(self.lineTabEdit)

        self.retranslateUi(EditSection)
        QtCore.QMetaObject.connectSlotsByName(EditSection)

    def retranslateUi(self, EditSection):
        EditSection.setWindowTitle(QtGui.QApplication.translate("EditSection", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditSection", "Change value:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditSection", "Row:", None, QtGui.QApplication.UnicodeUTF8))
        self.addRow.setText(QtGui.QApplication.translate("EditSection", "add", None, QtGui.QApplication.UnicodeUTF8))
        self.rmRow.setText(QtGui.QApplication.translate("EditSection", "rm", None, QtGui.QApplication.UnicodeUTF8))
        self.upRow.setText(QtGui.QApplication.translate("EditSection", "up", None, QtGui.QApplication.UnicodeUTF8))
        self.downRow.setText(QtGui.QApplication.translate("EditSection", "down", None, QtGui.QApplication.UnicodeUTF8))

