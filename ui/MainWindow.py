import sys
import os
from PyQt5.QtCore import pyqtSlot, QPoint, Qt, QRect,pyqtSignal
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QHBoxLayout,
                             QVBoxLayout, QTabWidget, QWidget, QAction,
                             QLabel, QSizeGrip, QMenuBar, qApp)
from PyQt5.QtGui import QIcon
#from .NommageTitleWindow import TitleWindow
from ..ui.UiNommage import Dialog

class mainWindow(QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setFixedSize(490, 490)
        #self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        #self.setStyleSheet("background-color: #FFB532;")

        """
        <a href='https://www.freepik.com/free-photos-vectors/technology'>Technology vector created by vectorpocket - www.freepik.com</a>
        """
        self.setWindowTitle('PyNetworks By CHIBANI IMAD')
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + '../ressources/optic.jpg'))
        #self.setWindowIcon(QIcon('./ressources/Circet.jpg'))

        self.title_bar = TitleWindow()
        self.dialog=Dialog()

        self.layout  = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.title_bar)
        self.dialog=Dialog()
        self.setNommageLayout()
        self.footer=footer()
        self.layout.addWidget(self.footer)

        #self.layout.addWidget(self.dialog)
        #self.layoutadded.connect(self.setNommageLayout(self.layout))
        #self.layout.addWidget(self.centralwindow)
        #self.layout.addWidget(self.dialog)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def setNommageLayout(self):
        self.layout.addWidget(self.dialog)

class footer(QWidget):
    height=25
    def __init__(self,parent=None):

        super(footer, self).__init__(parent=parent)
        self.layout=QHBoxLayout()
        self.layout.setContentsMargins(20,20,10,10)
        self.label=QLabel(wordWrap=True,alignment=Qt.AlignLeft|Qt.AlignTop)
        self.label.setOpenExternalLinks(True)
        urlLink="<a href=\"https://www.linkedin.com/in/imad-chibani-a8760712b/\"> Here</a>"
        self.label.setText("This software is copyrighted by default. People can read the code, but they have no legal right to use it. To use the code, you must contact the author directly and ask permission. For any further information you can contact the author "+urlLink)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

class TitleWindow(QWidget):
    addForm=pyqtSignal()
    #switch_window=pyqtSignal(str)
    height = 35
    def __init__(self,parent=None):

        super(TitleWindow, self).__init__(parent=parent)


        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
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

        self.NewAction.triggered.connect(self.addForm)


        self.layout.addWidget(self.Qmenu_bar)




        self.setLayout(self.layout)
        #self.setLayout(self.layout)


    def switch(self):
        self.switch_window.emit(self.line_edit.text())
