import sys
from PyQt5.QtCore import pyqtSlot, QPoint, Qt, QRect,pyqtSignal,QLocale,QDateTime
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QHBoxLayout,QDateTimeEdit,QTableWidget,QTableWidgetItem,QFileDialog,
                             QVBoxLayout, QTabWidget, QWidget, QAction,QGroupBox,QFormLayout,QSpinBox,QDialog,QDialogButtonBox,
                             QLabel, QSizeGrip, QMenuBar, qApp,QDateEdit, QCalendarWidget,QLineEdit,QComboBox ,QGridLayout, QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QIcon
from datetime import datetime
from ..modules.ReadBal import readBal

class Dialog(QDialog):


    def __init__(self):
        super(Dialog, self).__init__()

        self.createFormGroupBox()

        ValiderBtn=QPushButton()
        ValiderBtn.setText("Valider")
        ValiderBtn.setStyleSheet(self.stylesheet_for_ValiderPushbtn())
        ValiderBtn.setFixedSize(100,30)
        ValiderBtn.clicked.connect(self.getInformationFromForm)

        ResetBtn=QPushButton()
        ResetBtn.setText("Réanitialiser")
        ResetBtn.setStyleSheet(self.stylesheet_for_ValiderPushbtn())
        ResetBtn.setFixedSize(100,30)
        ResetBtn.clicked.connect(self.resetInformationFromForm)
        #buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        #buttonBox.accepted.connect(self.accept)
        #buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        BtnLayout=QHBoxLayout()

        mainLayout.addWidget(self.formGroupBox)
        BtnLayout.addWidget(ValiderBtn)
        BtnLayout.addWidget(ResetBtn)
        BtnLayout.addStretch(1)
        #mainLayout.addWidget(buttonBox)
        #self.creatingTables(mainLayout)
        mainLayout.addLayout(BtnLayout)
        self.setLayout(mainLayout)




    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Info PM")
        layout = QFormLayout()
        """-------------------------------------------- """
        self.EditorCommande=QLineEdit()
        self.EditorCommande.setStyleSheet(self.stylesheet_for_Edit())
        layout.addRow(QLabel("SRO-BPI:"), self.EditorCommande)
        """-------------------------------------------- """
        self.Emprise=QLineEdit()
        self.Emprise.setStyleSheet(self.stylesheet_for_Edit())
        layout.addRow(QLabel("N° PM:"), self.Emprise)
        """-------------------------------------------- """
        self.CodeCableSFR=QLineEdit()
        self.CodeCableSFR.setStyleSheet(self.stylesheet_for_Edit())
        layout.addRow(QLabel("Code Cable:"), self.CodeCableSFR)
        """-------------------------------------------- """
        #self.init_row(QPushButton(),"Export BAL",QLabel(),layout)
        self.Bal=QPushButton()
        self.Bal.setText("Export BAL")
        self.BalLink=QLabel()
        self.BalLink.setStyleSheet(self.stylesheet_for_Edit())
        layout.addRow(self.Bal,self.BalLink)
        self.Bal.clicked.connect(self.openFileLinkDialogForBal)
        """-------------------------------------------- """
        self.Syno=QPushButton()
        self.Syno.setText("Synoptique")
        self.SynoLink=QLabel()
        self.SynoLink.setStyleSheet(self.stylesheet_for_Edit())
        layout.addRow(self.Syno,self.SynoLink)
        self.Syno.clicked.connect(self.openFileLinkDialogForSyno)
        """-------------------------------------------- """
        self.Save=QPushButton()
        self.Save.setText("Save")
        self.SaveLink=QLabel()
        self.SaveLink.setStyleSheet(self.stylesheet_for_Edit())
        layout.addRow(self.Save,self.SaveLink)
        self.Save.clicked.connect(self.openFileLinkDialogForSaving)
        """-------------------------------------------- """
        self.formGroupBox.setLayout(layout)


    def stylesheet_for_Edit(self):
        stylesheet="""
        background-color: white;
        color: black;
        border: 2px solid #FF8C00;
        """
        return stylesheet
    def stylesheet_for_Pushbtn(self):
        stylesheet="""
        color: #000000;
        background-color: #FF9F0B;
        font-size: 14px;
        padding: 4px;
        """
        return stylesheet
    def stylesheet_for_ValiderPushbtn(self):
        stylesheet="""
        color: #000000;
        background-color: #FF9F0B;
        font-size: 14px;
        padding: 4px;
        margin-left:14px;
        """
        return stylesheet

    def getInformationFromForm(self):

        try:
            print("Do It")
            v1=readBal(self.BalLink.text(),self.Emprise.text(),self.SaveLink.text(),self.SynoLink.text(),self.EditorCommande.text(),self.CodeCableSFR.text()).readfile()
            print(v1)
        except:
            print("error")
    def resetInformationFromForm(self):
        self.BalLink.clear()
        self.Emprise.clear()
        self.SaveLink.clear()
        self.SynoLink.clear()
        self.EditorCommande.clear()
        self.CodeCableSFR.clear()

    def openFileLinkDialogForBal(self):
        options = QFileDialog.Options()
        self.fileLinkDialog = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "Open File","All Files (*);;Python Files (*.py)",options=options)
        if self.fileLinkDialog:
            #print(self.fileLinkDialog[0])
            self.BalLink.setText(self.fileLinkDialog[0])
            bal=self.fileLinkDialog[0]
            #print(bal.split("/"))

    def openFileLinkDialogForSyno(self):
        options = QFileDialog.Options()
        self.fileLinkDialog = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "Open File","All Files (*);;Python Files (*.py)",options=options)
        if self.fileLinkDialog:

            self.SynoLink.setText(self.fileLinkDialog[0])

    def openFileLinkDialogForSaving(self):
        options = QFileDialog.Options()

        self.fileLinkDialog = QFileDialog.getExistingDirectory(self,"Open Directory")
        if self.fileLinkDialog:

            self.SaveLink.setText(self.fileLinkDialog+"/"+str(self.Emprise.text())+".xlsx")
