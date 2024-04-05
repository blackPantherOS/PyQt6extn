import sys
from PySide2 import QtCore, QtWidgets, QtGui

from PySideExtn.SpiralProgressBar import spiralProgressBar #IMPORT THE EXTENSION LIBRARY

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.hello = 'Spiral Progress Bar'
        
        self.spbN = spiralProgressBar()    #SPIRAL PROGRESSBAR OBJECT
        self.spbN.spb_setNoProgressBar(4)

        #SETING THE INITIAL POSITION OF THE PROGRESS BAR: FROM OUTER-INWARDS
        self.spbN.spb_setInitialPos(('North', 'South', 'East', 'West'))

        self.spbN.spb_setValue((55, 65, 75, 85))

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.spbN)
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())