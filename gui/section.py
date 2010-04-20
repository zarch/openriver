# -*- coding: utf-8 -*-
"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qt import *

# Import the compiled UI module
from main import Ui_MainWindow
from importOri import Ui_importORI

# Import geometry from core
from sys import path
from os.path import join
path.append(join('..','core'))
import geometry as geo

class SectionPoint(QGraphicsEllipseItem):
    def __init__(self, window, index, data):
        self.window = window
        self.row = index

        self.data = data
        r = 5
        x, y, z, ks = self.data
        self.bbox = QRectF(y-r, -z-r, 2*r, 2*r)
        self.point = QPointF(y, -z)

        super(SectionPoint, self).__init__(self.bbox)
        self.setBrush(QBrush(QColor(0, 0, 150)))
        self.setFlag(QGraphicsItem.ItemIsSelectable)

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

        self.scene = QGraphicsScene(self)
        green = QColor(0, 150, 0)
        self.ui.sectionGraphics.setScene(self.scene)

        ksmin, ksmax = self.minmax_ks()
        self.ksmin, self.ksmax = ksmin, ksmax

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
        r = 5
        i = 0
        pen = QPen(QColor(150, 0, 0))

        pnt0 = SectionPoint(self, i, array[0])
        self.scene.addItem(pnt0)
        for data in array[1:]:
            i += 1
            pnt1 = SectionPoint(self, i, data)
            self.scene.addLine(QLineF(pnt0.point, pnt1.point), pen)
            self.scene.addItem(pnt1)
            pnt0 = pnt1

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

    def on_action_Open_triggered(self,checked=None):
        if checked is None: return
        filename = QFileDialog.getOpenFileName(self, 'Open project', '/home')
        print filename

    def on_actionImport_triggered(self,checked=None):
        if checked is None: return
        sectionsfilename = QFileDialog.getOpenFileName(self, 'Import sections.ori file', '/home')
        pointsfilename = QFileDialog.getOpenFileName(self, 'Import points.ori file', sectionsfilename)
        river = geo.Reach()
        river.importFileORI(sectionsfilename, pointsfilename)



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
