# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main.ui'
#
# Created: Sat Apr 17 13:15:52 2010
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
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 651, 192))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.listSections = QtGui.QListWidget(self.splitter)
        self.listSections.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listSections.setObjectName("listSections")
        self.tableSectionCoord = QtGui.QTableWidget(self.splitter)
        self.tableSectionCoord.setMinimumSize(QtCore.QSize(450, 0))
        self.tableSectionCoord.setMaximumSize(QtCore.QSize(256, 16777215))
        self.tableSectionCoord.setAlternatingRowColors(True)
        self.tableSectionCoord.setObjectName("tableSectionCoord")
        self.tableSectionCoord.setColumnCount(4)
        self.tableSectionCoord.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableSectionCoord.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableSectionCoord.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableSectionCoord.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableSectionCoord.setHorizontalHeaderItem(3, item)
        self.tableSectionCoord.horizontalHeader().setCascadingSectionResizes(True)
        self.splitter_2 = QtGui.QSplitter(self.splitter)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.sectionGraphics = QtGui.QGraphicsView(self.centralwidget)
        self.sectionGraphics.setGeometry(QtCore.QRect(0, 200, 651, 341))
        self.sectionGraphics.setObjectName("sectionGraphics")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menu_File.addAction(self.actionImport)
        self.menu_File.addAction(self.actionExport)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.listSections, QtCore.SIGNAL("currentTextChanged(QString)"), MainWindow.sectionChanged)
        QtCore.QObject.connect(self.listSections, QtCore.SIGNAL("currentRowChanged(int)"), MainWindow.itemChanged)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "openriver", None, QtGui.QApplication.UnicodeUTF8))
        self.tableSectionCoord.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.tableSectionCoord.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.tableSectionCoord.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.tableSectionCoord.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "ks", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))

