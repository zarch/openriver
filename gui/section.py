# -*- coding: utf-8 -*-
"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qt import *

# Import the compiled UI module
from main import Ui_MainWindow

# Import geometry from core
from sys import path
from os.path import join
path.append(join('..','core'))
import geometry as geo

class SectionPoint(QGraphicsEllipseItem):
    def __init__(self, window, point, *args):
        super(SectionPoint, self).__init__(*args)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.window = window
        self.row = point

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemSelectedChange:
            self.window.ui.tableSectionCoord.selectRow(self.row)
        return super(SectionPoint, self).itemChange(change, value)

# Create a class for our main window
class Main(QMainWindow):
    def __init__(self,  sezlist):
        QMainWindow.__init__(self)
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
        self.scene = QGraphicsScene(self)
        #self.scene.setSceneRect(0, 0, 10, 20)
        green = QColor(0, 150, 0)
        #self.scene.setBackgroundBrush(QtGui.QBrush(green))
        self.ui.sectionGraphics.setScene(self.scene)

        ksmin, ksmax = self.minmax_ks()
        self.ksmin, self.ksmax = ksmin, ksmax

#        #path = QPainterPath(0, 10, 0, 0, 20, 5)
#        rect0 = QRectF(0, 0, 200, 50)
#        rect1 = QRectF(0, 0, 20, 50)
#        pen = QPen(QtGui.QColor(150, 0, 0))
#        brush = QBrush(QtGui.QColor(0, 0, 150))
#        pnt = QPointF
#        pnt0 = pnt(0, 0)
#        pnt1 = pnt(-200, 200)
#        line0 = QLineF(pnt0, pnt1)
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
                item = QTableWidgetItem()
                item.setText(str(array[i][j]))
                self.ui.tableSectionCoord.setItem(i,j,item)

    def drawSection(self, array):
        self.scene.clear()
#        kslist = array.T[3]
#        ksmax = max(kslist)
#        ksmin = min(kslist)
        r = 5
        x, y, z, ks = array[0]
        i = -1
        pnt0 = QPointF(y, -z)
        #pnt0.setFlags(QGraphicsItem.ItemIsSelectable)
        rect0 = QRectF(y-r, -z-r, 2*r, 2*r)
        for x, y, z, ks in array[1:]:
            pen = QPen(QColor(150, 0, 0))
            brush = QBrush(QColor(0, 0, 150))
            pnt1 = QPointF(y, -z)
            line = QLineF(pnt0, pnt1)
            self.scene.addLine(line, pen)
            #self.scene.addEllipse(rect0, pen, brush)
            i += 1
            self.scene.addItem(SectionPoint(self, i, rect0))
            pnt0 = pnt1
            rect0 = QRectF(y-r, -z-r, 2*r, 2*r)
        #self.scene.addEllipse(rect0, pen, brush)
        i += 1
        self.scene.addItem(SectionPoint(self, i, rect0))

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

    app = QApplication(sys.argv)
    window=Main(river.sections)
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
