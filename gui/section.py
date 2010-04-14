# -*- coding: utf-8 -*-
"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from main import Ui_MainWindow



# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self,  sezlist):
        QtGui.QMainWindow.__init__(self)
        #self.coords = coords
        self.sezlist = sezlist

        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #populate the list section
        self.ui.listSections.insertItems(0, self.sezlist)
        self.connect(self, SIGNAL('currentChanged()'), self.item_changed)
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
    coordsez0 = [[0.,0.,10.,20.],
                 [0.,5.,0.,20.],
                 [0.,10.,0.,20.],
                 [0.,15.,12.,20.],]
    sezlist = ['sez0', 'sez1', 'sez2', 'sez3', 'sez4',]

    app = QtGui.QApplication(sys.argv)
    window=Main(sezlist)
    window.viewTable(coordsez0)
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
