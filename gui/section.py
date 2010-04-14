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
#        self.connect(self, SIGNAL('currentChanged()'), self.item_changed)
#        if self.ui.listSections.currentItemChanged():
#            sez = self.ui.listSections.currentItem()
#            print sez
#            #viewTable(sez.coords)

    def item_changed(self):
             item = self.currentItem()
             print item
#             viewTable(item.coords)

    def viewTable(self, array):
        # Let's do something interesting: load section coordinates
        # into our table widget
        self.ui.tableSectionCoord.setRowCount(len(array))
        for i, row in enumerate(array):
            for j, numb in enumerate(row):
                item = QtGui.QTableWidgetItem()
                item.setText(str(array[i][j]))
                self.ui.tableSectionCoord.setItem(i,j,item)




def main():
    # Define coordinate list
    sezdata=[[0.000, 0.930,  7.190, 12.590, 18.080, 18.910, 20.070],
[747.27000, 742.79000, 742.77000, 742.75000, 742.73000, 742.73000, 747.28000]]
    # create different section
    sez0 = geo.Section(name = 'sez0', yzcoord=sezdata)
    sez1 = geo.Section(name = 'sez1', yzcoord=sezdata)
    sez2 = geo.Section(name = 'sez2', yzcoord=sezdata)
    sez3 = geo.Section(name = 'sez3', yzcoord=sezdata)
    sez4 = geo.Section(name = 'sez4', yzcoord=sezdata)
    print sez0, sez1, sez2, sez3, sez4
    # create a list of section
    sezlist = [sez0, sez1, sez2, sez3, sez4,]

    app = QtGui.QApplication(sys.argv)
    window=Main(sezlist)
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
