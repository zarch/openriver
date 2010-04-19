# -*- coding: utf-8 -*-
"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4 import QtCore,QtGui, Qt

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

#        self.view = self.ui.sectionGraphics
        self.scene = QtGui.QGraphicsScene(self)
        #self.scene.setSceneRect(0, 0, 10, 20)
        green = QtGui.QColor(0, 150, 0)
        #self.scene.setBackgroundBrush(QtGui.QBrush(green))
        self.ui.sectionGraphics.setScene(self.scene)

        ksmin, ksmax = self.minmax_ks()
        self.ksmin, self.ksmax = ksmin, ksmax

#        #path = QtGui.QPainterPath(0, 10, 0, 0, 20, 5)
#        rect0 = QtCore.QRectF(0, 0, 200, 50)
#        rect1 = QtCore.QRectF(0, 0, 20, 50)
#        pen = QtGui.QPen(QtGui.QColor(150, 0, 0))
#        brush = QtGui.QBrush(QtGui.QColor(0, 0, 150))
#        pnt = QtCore.QPointF
#        pnt0 = pnt(0, 0)
#        pnt1 = pnt(-200, 200)
#        line0 = QtCore.QLineF(pnt0, pnt1)
#        self.scene.addRect(rect0, pen, brush)
#        self.scene.addEllipse(rect1, pen, brush)
#        self.scene.addLine(line0, pen)


    def itemChanged(self, index):
        coord = self.sezlist[index].coord
        self.viewTable(coord)
        self.drawSection(coord)

    def viewTable(self, array):
        # Let's do something interesting: load section coordinates
        # into our table widget
        self.ui.tableSectionCoord.setRowCount(len(array))
        for i, row in enumerate(array):
            for j, numb in enumerate(row):
                item = QtGui.QTableWidgetItem()
                item.setText(str(array[i][j]))
                self.ui.tableSectionCoord.setItem(i,j,item)

    def drawSection(self, array):
        self.scene.clear()
#        kslist = array.T[3]
#        ksmax = max(kslist)
#        ksmin = min(kslist)
        r = 5
        x, y, z, ks = array[0]
        pnt0 = QtCore.QPointF(y, -z)
        #pnt0.setFlags(QtGui.QGraphicsItem.ItemIsSelectable)
        rect0 = QtCore.QRectF(y-r, -z-r, 2*r, 2*r)
        for x, y, z, ks in array[1:]:
            pen = QtGui.QPen(QtGui.QColor(150, 0, 0))
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 150))
            pnt1 = QtCore.QPointF(y, -z)
            line = QtCore.QLineF(pnt0, pnt1)
            self.scene.addLine(line, pen)
            #self.scene.addEllipse(rect0, pen, brush)
            sezpnt = QtGui.QGraphicsEllipseItem(rect0)
            sezpnt.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(sezpnt)
            pnt0 = pnt1
            rect0 = QtCore.QRectF(y-r, -z-r, 2*r, 2*r)
        #self.scene.addEllipse(rect0, pen, brush)
        sezpnt = QtGui.QGraphicsEllipseItem(rect0)
        sezpnt.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
        self.scene.addItem(sezpnt)

    def minmax_ks(self):
        """Return min and max of ks looking from all sections"""
        min = 0
        max = 0
        for s in self.sezlist:
            kslist = s.coord.T[3]
            min0 = kslist.min()
            max0 = kslist.max()
            min = min if min < min0 else min0
            max = max if max > max0 else max0
        return min, max


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
