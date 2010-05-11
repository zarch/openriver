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
from viewSimulation2 import Ui_MainWindow as Ui_viewSimulation1D

# Import geometry from core
from sys import path
from os.path import join as joinpath
import os as os
import glob as glob
import fnmatch as fnmatch
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
    def __init__(self, window, index=None, data=None, point=None):
        self.window = window
        self.row = index
        self.data = data
        r = 5
        #print 'data:',  self.data
        if not data==None:
            x, y, z, ks = self.data
            self.point = QPointF(y, z)
        else:
            self.point = point
        #print self.point.x(), self.point.y()
        
        self.bbox = QRectF(self.point.x()-r, -self.point.y()+r, 2*r, 2*r)

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
        #print '='*40
        #print limit
        for i, l in enumerate(limit):
            if ratio >= l:
         #       print ratio, l, i
                cl = i
        #print 'cl is:', cl
        return cl

    def getColorStyle(self, ks, pen):
        # Fraction to choose color and line 'color:width:dash:zigzag'
        r = (ks - self.ksmin)/(self.ksmax - self.ksmin)
        # classification in 5 different class
        cl = self.classify(r, 5)
        #print 'r is:%s\nks is:%s\nclass is %s' % (r, ks, str(cl))
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
        pnt0 = SectionPoint(self, index=i, data=array[0])
        # get firs ks
        x, y, z, ks = array[0]
        self.scene.addItem(pnt0)
        for data in array[1:]:
            i += 1
            pnt1 = SectionPoint(self, index=i, data=data)
            # change pen property
            pen0 = self.getColorStyle(ks, pen)
            self.scene.addItem(pnt1)
            self.scene.addLine(QLineF(pnt0.point, pnt1.point), pen0)
            #print pnt0.point,pnt1.point
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
       # print filename

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

    def on_actionView_triggered(self, checked=None):
        if checked is None: return
        viewer = ViewSimulation(self, self.sezlist, plane='xz', drawpoints=False)
        
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

class PolyLine():
    """Return a scene with points and lines
    x = [x0,x1,x2,...,xn]
    y = [[a0,a1,a2,...,an],
         [b0,b1,b2,...,bn],
         [c0,c1,c2,...,cn]]
    pen = [penA,penB,penC]


    >>> xp = [1, 2, 3, 4, 5]
    >>> yp = [[0, 2, 4, 6, 8],
              [0, 2, 3, 4, 5],
              [7, 5, 3, 1, 0]]
    """
    def __init__(self, scene, pens, x=None, y=None,  lines = None, drawpoints=False):
        self.scene = scene
        self.x = x
        self.y = y
        self.pens = pens
        self.lines = lines
        if not lines:
            self.lines = self.getLines()
        self.drawpoints = drawpoints

############################
# TODO verify this function probably it's broken.
    def getLines(self):
        """Return lines from x and y list
        lines = [line1,line2,line3]
        line1 = [[x0,a0],[x1,a1],...,[xn,an]]
        line2 = [[x0,b0],[x1,b1],...,[xn,bn]]
        line3 = [[x0,c0],[x1,c1],...,[xn,cn]]"""
        lines = []
        yT = np.array(self.y).T
        for y in yT:
            #print 'y:', y
            line = []
            for xi, yi in zip(self.x, y):
                p = xi, yi
                line.append(p)
            #print 'line:', line
            lines.append(line)
        lines = np.array(lines)
        return lines

    def drawPolines(self):
        #print len(self.lines), len(self.pens)
        #print self.lines[0]
        for line,pen  in zip(self.lines, self.pens):
            self.drawLine(line, pen)

    def drawLine(self, line, pen):
        """Add line to a scene

        line is define as:
        line = [(x0,y0),(x1,y1),...,(xn,yn)]"""
        #print 'line:', line
        x0, y0 = line[0]
        pnt0 = QPointF(x0, y0)
        if self.drawpoints:
            p0 = SectionPoint(self, point = pnt0)
            self.scene.addItem(p0)
        for x1, y1 in line[1:]:
            pnt1 = QPointF(x1, y1)
            self.scene.addLine(QLineF(pnt0, pnt1), pen)
            pnt0 = pnt1
            if self.drawpoints:
                p0 = SectionPoint(self, point = pnt0)
                self.scene.addItem(p0)

class ViewSimulation(QMainWindow):
    def __init__(self, parent=None, sectionlist=None,  plane = 'xz', drawpoints=True):
        super(ViewSimulation, self).__init__(parent)
        self.ui = Ui_viewSimulation1D()
        self.ui.setupUi(self)
        self.sectionlist = sectionlist
        self.readSimulation()
        self.plane = plane
        self.drawpoints = drawpoints
        self.scene = QGraphicsScene(self)
        self.ui.GraphicSimulation1D.setScene(self.scene)
        self.show()
        
    def itemChanged(self, index):
        self.scene.clear()
        profile = self.profilesName[index]
        wsData = np.genfromtxt(profile)
        rows = wsData.shape[0]
        for m in range(0,rows):
           self.sectionlist[m].watersurf = wsData[m][0]
        print "changed"
        self.drawLines()

    def getPointsPlane(self, section):
        """plane could be 'xz' or 'xy' """
        if self.plane == 'xz':
            plane = 2
        elif self.plane == 'xy':
            plane = 1
        data = section.data
        x = float(section.xcoord[0])
        talweg = float(section.min)
        watersurface = section.watersurf
        bank_l = float(data[0][plane])
        bank_r = float(data[-1][plane])
        return x, [talweg, watersurface, bank_l, bank_r]

    def drawLines(self):
        """Generic function to add line to the scene, specify index (for examples, min, banks,)"""
        x, y = [], []
        for sect in self.sectionlist:
            xn, yn = self.getPointsPlane(sect)
            x.append(xn)
            y.append(yn)
        pen_talweg = QPen(Qt.darkRed)
        pen_water = QPen(Qt.darkBlue)
        pen_bank_l = QPen(Qt.black)
        pen_bank_r = QPen(Qt.black)
        pen_bank_r.setStyle(Qt.DotLine)
        pens = [pen_talweg, pen_water, pen_bank_l, pen_bank_r]
        lines = PolyLine(self.scene, pens, x, y, drawpoints=self.drawpoints)
        lines.drawPolines()
        self.ui.GraphicSimulation1D.setScene(lines.scene)
        
    def readSimulation(self):
        self.profilesName = []
        paths =  str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        files = os.listdir(paths)
        for file in files:
            if glob.fnmatch.fnmatch(file,"res*"):
               self.profilesName.append(str(paths)+"/"+str(file))
            if glob.fnmatch.fnmatch(file,"time*"):
                timesName = str(paths)+"/"+str(file)
        self.timesList = []
        timesData = np.genfromtxt(timesName)
        rows = timesData.shape[0]
        for m in range(0,rows):
            self.timesList.append(str(timesData[m][1]))
        self.profilesName = sorted(self.profilesName)
        self.ui.listProfiles.insertItems(0, self.timesList)

        
#        resultsfilename = QFileDialog.getOpenFileName(self, 'Select results file', '/home')
#        resultsfilename = str(resultsfilename)
#        resultsData = np.genfromtxt(resultsfilename)
#        rows = resultsData.shape[0]
#        for m in range(0,rows):
#           self.sectionlist[m].watersurf = resultsData[m][0]

def main():
    # import a reach for test
    river = geo.Reach()
    river.importFileOri('../test/test3/sections.ori', '../test/test3/points.ori')
    app = QApplication(sys.argv)
    window = Main(river.sections)
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
