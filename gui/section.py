# -*- coding: utf-8 -*-
"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qt import *
import numpy as np

# Import the compiled UI module
from main import Ui_MainWindow
from importOri import Ui_importORI
from editPoints import Ui_EditSection
from viewSimulation import Ui_viewSimulation1D

# Import geometry from core
from sys import path
from os.path import join as joinpath
path.append(joinpath('..','core'))
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
        return super(SectionPoint, self).itemChange(change, value)

# Create a class for our main window
class Main(QMainWindow):
    def __init__(self,  sezlist):
        QMainWindow.__init__(self)
        self.sezlist = sezlist

        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        # populate the list section
        listsect = []
        for s in self.sezlist:
            listsect.append(str(s))
        self.ui.listSections.insertItems(0, listsect)

        self.scene = QGraphicsScene(self)
        green = QColor(0, 150, 0)
        self.ui.sectionGraphics.setScene(self.scene)

        # take line edit from the UI and set data type Validation
        self.edit = self.ui.lineTabEdit
        float_validator = QDoubleValidator(-999999.0, 999999.0, 3, self.edit)
        self.edit.setValidator(float_validator)

        self.ksmin, self.ksmax = self.minmax_ks()
        # define how section line should be draw
        self.kslinestyle = 'color:width:dash' # 'color:width:dash:zigzag'

    def itemChanged(self, index):
        sect = self.sezlist[index]
        coord = sect.data
        self.sectionModel = SectionModel(coord)
        self.ui.tableSectionCoord.setModel(self.sectionModel)

        self.connect(self.sectionModel, SIGNAL("dataChanged(QModelIndex, QModelIndex)"), self.dataModelChanged)
        self.drawSection(coord)

    def dataModelChanged(self, index, index2):
        self.drawSection(self.sectionModel.array)

    def classify(self, ratio, numberOfClass):
        """
        Return classification of a number given the number of class

        >>> classify(1., 5)
        4
        >>> classify(0., 5)
        0
        >>> classify(0.3, 5)
        1
        >>> classify(0.5, 5)
        2
        """
        cl = 0
        pas = 1./numberOfClass
        limit = np.array([i for i in range(numberOfClass)]) * pas
        print '='*40
        print limit
        for i, l in enumerate(limit):
            if ratio >= l:
                print ratio, l, i
                cl = i
        print 'cl is:', cl
        return cl

    def getColorStyle(self, ks, pen):
        # Fraction to choose color and line 'color:width:dash:zigzag'
        r = (ks - self.ksmin)/(self.ksmax - self.ksmin)
        # classification in 5 different class
        cl = self.classify(r, 5)
        print 'r is:%s\nks is:%s\nclass is %s' % (r, ks, str(cl))
        if 'color' in self.kslinestyle:
            pen.setColor(QColor(int(250*(1-r)), 0, 0))
        if 'width' in self.kslinestyle:
            pen.setWidth(4-cl)
        if 'dash' in self.kslinestyle:
            dashstyle = {0 : Qt.SolidLine,
                         1 : Qt.DashLine,
                         2 : Qt.DashDotLine,
                         3 : Qt.DashDotDotLine,
                         4 : Qt.DotLine}
            pen.setStyle(dashstyle[4-cl])
        return pen

    def drawSection(self, array):
        self.scene.clear()
        r = 5
        i = 0
        pen = QPen(QColor(0, 0, 0))
        # initialize first point
        pnt0 = SectionPoint(self, i, array[0])
        # get firs ks
        x, y, z, ks = array[0]
        self.scene.addItem(pnt0)
        for data in array[1:]:
            i += 1
            pnt1 = SectionPoint(self, i, data)
            # change pen property
            pen0 = self.getColorStyle(ks, pen)
            self.scene.addLine(QLineF(pnt0.point, pnt1.point), pen0)
            self.scene.addItem(pnt1)
            pnt0 = pnt1
            x, y, z, ks = data

    def minmax_ks(self):
        """Return min and max of ks looking from all sections"""
        min = 0
        max = 0
        for s in self.sezlist:
            kslist = s.data.T[3]
            min0 = kslist.min()
            max0 = kslist.max()
            min = min if min < min0 else min0
            max = max if max > max0 else max0
        return min, max

    def on_actionOpen_triggered(self,checked=None):
        if checked is None: return
        filename = QFileDialog.getOpenFileName(self, 'Open project', '/home')
        print filename

    def on_actionImport_triggered(self,checked=None):
        if checked is None: return
        sectionsfilename = QFileDialog.getOpenFileName(self, 'Import sections.ori file', '/home')
        pointsfilename = QFileDialog.getOpenFileName(self, 'Import points.ori file', sectionsfilename)
        river = geo.Reach()
        river.importFileORI(sectionsfilename, pointsfilename)

    def on_actionRun_triggered(self,checked=None):
        if checked is None: return
        # TODO:
        #    * add command to compile?
        #    * or make /bin directory and check which system (32/64 bit) is running and which OS? and then run the comand?
        os.system('./../core/fixbed_sw_1D.out')

#-----------
    def getSimulationPoints(self, section):
        data = section.data
        x = float(section.xcoord[0])
        
        talweg = -float(section.min)
        watersurface = talweg
        #watersurface = sect.watersurf[t]
        bank_l = -float(data[0][2])
        bank_r = -float(data[-1][2])
        #points.append([sect.x, talweg, watersurface, bank_l, bank_r])
        p_talweg= QPointF(x, talweg)
        p_watersurface = QPointF(x, watersurface)
        p_bank_l = QPointF(x, bank_l)
        p_bank_r = QPointF(x, bank_r)
        return [p_talweg, p_watersurface, p_bank_l, p_bank_r]

    def drawLines(self):
	    """Generic function to add line to the scene, specify index (for examples, min, banks,)"""
	    #x0, y0, z0, ks0 = sectionlist[0].data[index]
	    #pnt0 = QPointF(x0, z0)
	    #points = []
	    print "djfhvbzvldz"
	    pen = QPen(QColor(0, 0, 0))
	    # TODO differentiate pens
	    sect0 = self.sezlist[0]
	    points0 = self.getSimulationPoints(sect0)
	    for sect in self.sezlist[1:]:
		    points1 = self.getSimulationPoints(sect)
		    for i in range(4):
			    self.scene.addLine(QLineF(points0[i], points1[i]), pen)
		    points0 = points1
	    self.ui.sectionGraphics.setScene(self.scene)
#------

    def on_actionView_triggered(self, checked=None):
        if checked is None: return
        self.scene.clear()
        self.drawLines()
        
        #viewer = ViewSimulation1D(self, self.sezlist)
        #self.ui.sectionGraphics.setScene(viewer.getScene())

    def on_lineTabEdit_returnPressed(self, checked=None):
        # selectedIndexes() returns a list of all selected and non-hidden item indexes in the view
        cellist = self.ui.tableSectionCoord.selectedIndexes()
        newvalue = self.edit.text()
        #print self.sectionModel.array
        for cel in cellist:
            self.sectionModel.setData(cel, newvalue)
        self.edit.clear()

class SectionEditor(QWidget):
    def __init__(self, parent, task=None):
        super(SectionEditor, self).__init__(parent)

        self.ui = Ui_EditSection()
        self.ui.setupUi(self)

#class ViewSimulation1D(QWidget):
#    #def __init__(self, parent, sectionlist=None):
#    def __init__(self, window, sectionlist=None):
#        #super(ViewSimulation1D, self).__init__(parent)
#		self.window = window
#		self.ui = Ui_viewSimulation1D()
#		self.ui.setupUi(self)

#		self.sectionlist = sectionlist

#		self.scene = QGraphicsScene(self)

#		self.ui.GraphicSimulation1D.setScene(self.scene)

#    def getScene(self):
#        self.drawLines()
#        return self.scene

#    def getPoints(self, section):
#		data = sect.data
#		talweg = data[sect.min]
#		watersurface = talweg
#		#watersurface = sect.watersurf[t]
#		bank_l = data[0]
#		bank_r = data[-1]
#		#points.append([sect.x, talweg, watersurface, bank_l, bank_r])
#		p_talweg= QPointF(sect.x, talweg)
#		p_watersurface = QPointF(sect.x, watersurface)
#		p_bank_l = QPointF(sect.x, bank_l)
#		p_bank_r = QPointF(sect.x, bank_r)
#		return [p_talweg, p_watersurface, p_bank_l, p_bank_r]

#    def drawLines(self):
#        """Generic function to add line to the scene, specify index (for examples, min, banks,)"""
#        #x0, y0, z0, ks0 = sectionlist[0].data[index]
#        #pnt0 = QPointF(x0, z0)
#        #points = []
#        points0 = self.getPoints(self.sectionlist[0])
#        for sect in self.sectionlist[1:]:
#            points1 = self.getPoints(sect)
#            for i in range(4):
#                self.scene.addLine(QLineF(points0[i], points1[i]), pen)
#            points0 = points1
#        self.window.ui.sectionGraphics.setScene(self.scene)



def main():
    # import a reach for test
    river = geo.Reach()
    river.importFileOri('../test/test1/sections.ori', '../test/test1/points.ori')

    app = QApplication(sys.argv)
    window = Main(river.sections)
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
