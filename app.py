import sys
from .ui.NommageTitleWindow import TitleWindow
from .ui.MainWindow import mainWindow
#from SecondWindow import WindowTwo
import sys
from PyQt5.QtCore import pyqtSlot, QPoint, Qt, QRect,pyqtSignal
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QHBoxLayout,
                             QVBoxLayout, QTabWidget, QWidget, QAction,
                             QLabel, QSizeGrip, QMenuBar, qApp)
from PyQt5.QtGui import QIcon

class Controller:
    def __init__(self):
        pass
    def show_main(self):
        self.window= mainWindow()
        #self.window.switch_window.connect(self.show_window_two)
        self.window.show()

    def show_window_two(self,text):
        self.window_two=WindowTwo(text)
        self.window.close()
        self.window_two.show()

def run():
    app=QApplication(sys.argv)
    controller=Controller()
    controller.show_main()
    #controller.show_window_two("Imad")
    sys.exit(app.exec_())

#if __name__=='__main__':
#    main()
