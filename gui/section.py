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

class SectionModel(QAbstractTableModel):
    def __init__(self, array):
        super(SectionModel, self).__init__()
        self.array = array

    def rowCount(self, parent=QModelIndex()):
        return len(self.array)

    def columnCount(self, parent=QModelIndex()):
        return max(map(len, self.array))

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            ret = self.array[index.row()][index.column()]
            # TODO: with "float()", it doesn't show any decimal, if ".0"
            return QVariant(str(ret))
        return QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self.array[index.row()][index.column()] = float(value.toDouble()[0])
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        ret = super(SectionModel, self).flags(index)
        ret |= Qt.ItemIsEditable
        return ret

    def headerData(self, col, orientation, role=Qt.DisplayRole):
        sections = ["x", "y", "z", "ks"]
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return QVariant(sections[col])
            elif orientation == Qt.Vertical:
                #return QVariant(col + 1)
                return super(SectionModel, self).headerData(col, orientation, role)
        return QVariant()

    # Models that provide interfaces to resizable data structures can provide
    # implementations of insertRows(), removeRows(), insertColumns(), and
    # removeColumns(). When implementing these functions, it is important to
    # call the appropriate functions so that all connected views are aware of
    # any changes:
    # * An insertRows() implementation must call beginInsertRows() before
    #   inserting new rows into the data structure, and it must call
    #   endInsertRows() immediately afterwards.
    # * An insertColumns() implementation must call beginInsertColumns()
    #   before inserting new columns into the data structure, and it must call
    #   endInsertColumns() immediately afterwards.
    # * A removeRows() implementation must call beginRemoveRows() before the
    #   rows are removed from the data structure, and it must call endRemoveRows()
    #   immediately afterwards.
    # * A removeColumns() implementation must call beginRemoveColumns() before the
    #   columns are removed from the data structure, and it must call
    #   endRemoveColumns() immediately afterwards.

    # http://doc.trolltech.com/4.6/model-view-model-subclassing.html
    # http://doc.trolltech.com/4.6/qabstracttablemodel.html

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
            self.window.ui.tableSectionCoordView.selectRow(self.row)
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
        self.sectionModel = SectionModel(coord)
        self.ui.tableSectionCoordView.setModel(self.sectionModel)

        self.connect(self.sectionModel, SIGNAL("dataChanged(QModelIndex, QModelIndex)"), self.dataModelChanged)
        self.viewTable(coord)
        self.drawSection(coord)

    def dataModelChanged(self, index, index2):
        self.drawSection(self.sectionModel.array)

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
