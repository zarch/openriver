# -*- coding: utf-8 -*-
"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from main import Ui_MainWindow

# Import geometry from core
from sys import path
from os.path import join
path.append(join('..','core'))
import geometry as geo



# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self,  sezlist):
        QtGui.QMainWindow.__init__(self)
        self.sezlist = sezlist

        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #populate the list section
        listsect = []
        for s in self.sezlist:
            listsect.append(str(s))
        self.ui.listSections.insertItems(0, listsect)

        self.scene = self.ui.sectionGraphics



    def itemChanged(self, index):
        coord = self.sezlist[index].coord
        self.viewTable(coord)

    def viewTable(self, array):
        # Let's do something interesting: load section coordinates
        # into our table widget
        self.ui.tableSectionCoord.setRowCount(len(array))
        for i, row in enumerate(array):
            for j, numb in enumerate(row):
                item = QtGui.QTableWidgetItem()
                item.setText(str(array[i][j]))
                self.ui.tableSectionCoord.setItem(i,j,item)

    def sectionChanged(self, text):
        print repr(text)

    def drawSection(self, array):
#        item = QtGui.QGraphicsItem()
#        item.setFlags(QGraphicsItem.ItemIsSelectable)
#        item.setPos(QPoint(array[0][1:3]))
        y, z = array[0][1:3]
        #print y,  z
        item = Pnt(y, z)
        #self.scene.clearSelection()
        self.scene.addItem(item)

class Pnt(QtGui.QGraphicsItem):
    def __init__(self, y, z):
        super(Pnt, self).__init__()
        self.rect = QtCore.QRectF(-30, -20, 60, 40)
        #self.color = color
        #print position
        self.setPos(y, z)

    def shape(self):
        path = QPainterPath()
        path.addEllips(self.rect)
        return path


def main():
    # import a reach for test
    river = geo.Reach()
    river.importFileORI('../test/test1/sections.ori', '../test/test1/points.ori')

    app = QtGui.QApplication(sys.argv)
    window=Main(river.sections)
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
