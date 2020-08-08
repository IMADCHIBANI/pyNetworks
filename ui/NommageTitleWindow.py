import sys
from PyQt5.QtCore import pyqtSlot, QPoint, Qt, QRect,pyqtSignal
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QHBoxLayout,
                             QVBoxLayout, QTabWidget, QWidget, QAction,QMessageBox,
                             QLabel, QSizeGrip, QMenuBar, qApp)
from PyQt5.QtGui import QIcon
from .UiNommage import Dialog
#from .MainWindow import mainWindow
#from .MainWindow import MainWindow

class TitleWindow(QWidget):

    switch_window=pyqtSignal(str)
    height = 35
    def __init__(self):

        QWidget.__init__(self)


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.Qmenu_bar=QMenuBar()
        self.Qmenu_bar.setStyleSheet("""
            color: #000000;
            background-color: #FF8C00;
            font-size: 14px;
            padding: 4px;
        """)
        #self.setCentralWidget(self.Qmenu_bar)
        self.file_menu=self.Qmenu_bar.addMenu('PyNetworks')
        #self.file_Settings=self.Qmenu_bar.addMenu('Settings')

        #self.action="print"
        #self.layout.addWidget(self.dialog)  MainWindow.setNommageLayout(layout)
        self.NewAction=QAction('Nommage Networks',self)
        self.PyNetworkssAct=self.file_menu.addAction(self.NewAction)
        self.btnAction=QPushButton()
        self.NewAction.triggered.connect(self.close)


        layout.addWidget(self.Qmenu_bar)


        self.setLayout(layout)
        #self.setLayout(self.layout)


    def switch(self):
        self.switch_window.emit(self.line_edit.text())
