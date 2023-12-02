# importing the required libraries 

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow #  for setting opacity
from PyQt6.QtWidgets import QWidget

class Ui_Sina(object):
    
    def setupUi(self, Sina):
        
        
        Sina.setObjectName("Sina")
        Sina.resize(363, 484)
        
        Sina.setMinimumSize(QtCore.QSize(363, 484))  # setting the Minimum Size of window
        Sina.setMaximumSize(QtCore.QSize(363, 484))  # setting the Maximum Size of window 
        font = QtGui.QFont()
        font.setPointSize(12)
        Sina.setFont(font)
        
        Sina.setStyleSheet("background-color: rgb(0, 0, 0);")
        Sina.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))

        self.Icn = QtGui.QIcon('Game.png')  #  We call QIcon class from the QtGui module and give it the icon 
        QWidget.setWindowIcon(Sina, self.Icn)
        
        
### ==========================================================================================================================
     
        
        self.btn = QtWidgets.QPushButton(parent=Sina)
        self.btn.setGeometry(QtCore.QRect(70, 224, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn.setFont(font)
   ### CSS code
        self.btn.setStyleSheet("QPushButton{\n"
                                "color: rgb(167, 209, 41);\n"
                                "background-color: rgb(62, 67, 46) ;\n"
                                "border-radius:29px;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover{background-color: rgb(77, 83, 57); }\n"
                                "\n"
                                "QPushButton:pressed{background-color: rgb(64, 69, 21) ; }\n"
                                "")
        self.btn.setObjectName("btn")
        self.btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        
        
        
        
        
        
        self.linE = QtWidgets.QLineEdit(parent=Sina)
        self.linE.setGeometry(QtCore.QRect(140, 150, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.linE.setFont(font)
        self.linE.setStyleSheet("color: rgb(174, 218, 42);\n"
                                "border: 3px solid rgb(97, 111, 57)")
        self.linE.setText("")
        self.linE.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.linE.setObjectName("linE")
        
        
        
        
        self.lab1 = QtWidgets.QLabel(parent=Sina)
        self.lab1.setGeometry(QtCore.QRect(40, 10, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lab1.setFont(font)
        self.lab1.setStyleSheet("color: rgb(167, 209, 41);")
        self.lab1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab1.setObjectName("lab1")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Sina)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 320, 221, 95))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 3)
        self.verticalLayout.setSpacing(27)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        
        self.lbl4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl4.setFont(font)
        self.lbl4.setStyleSheet("color: rgb(167, 209, 41);\n"
                                "border: 3px solid rgb(97, 111, 57);")
        self.lbl4.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.lbl4.setText("")
        self.lbl4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl4.setObjectName("lbl4")
        self.verticalLayout.addWidget(self.lbl4)
        
        
        
        self.lbl5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl5.setFont(font)
        self.lbl5.setStyleSheet("color: rgb(167, 209, 41);\n"
                                "border: 3px solid rgb(97, 111, 57);")
        self.lbl5.setText("")
        self.lbl5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl5.setObjectName("lbl5")
        self.verticalLayout.addWidget(self.lbl5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Sina)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 70, 131, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        
        
        
        self.lab2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lab2.setFont(font)
        self.lab2.setStyleSheet("color: rgb(167, 209, 41);")
        self.lab2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab2.setObjectName("lab2")
        self.verticalLayout_2.addWidget(self.lab2)
        
        
        
        
        self.lab3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lab3.setFont(font)
        self.lab3.setStyleSheet("color: rgb(167, 209, 41);")
        self.lab3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab3.setObjectName("lab3")
        self.verticalLayout_2.addWidget(self.lab3)
        
        
### ================= opacity ========================================================   
        self.objMain = QMainWindow(Sina)  # seting  QMainWindow object
        
        self.ItemOpcyity = float(1.0)
        
        self.objMain.setWindowOpacity(self.ItemOpcyity)  # setting opacity level
      
### =====================================================================================
       

        self.retranslateUi(Sina)
        
        
## ====================== signal ========================================  
   
        self.btn.clicked.connect(lambda: self.getOpacity())
        
               
### ============= func ===========================================
       
    def getOpacity(self):
        
        try:
                Sina.setWindowOpacity(float(self.linE.text()))        
                self.lbl4.setText('input number :  '+self.linE.text())
                
                exactPcty1 = round(Sina.windowOpacity(), 3)  # The exact number of Opacity and round to 3 flat !!!
                exactPcty2 = str(exactPcty1) 
                self.lbl5.setText('exact Opacity : '+ exactPcty2)
                
        except ValueError:      
               self.lbl4.setText(self.linE.text()) 
               self.lbl5.setText("Plese float only !!!")
                
    #def bastan(self):
        #self.close()

    def retranslateUi(self, Sina):
        _translate = QtCore.QCoreApplication.translate
        
        Sina.setWindowTitle(_translate("Sina", " Opacity Game"))  # set the title
        self.btn.setText(_translate("Sina", "Click"))
        self.lab1.setText(_translate("Sina", "Enter Opacity:"))
        self.lab2.setText(_translate("Sina", "Plese float"))
        self.lab3.setText(_translate("Sina", "< 0 , 1 >"))
        
        
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sina = QtWidgets.QWidget()
    ui = Ui_Sina()
    ui.setupUi(Sina)
    Sina.show()
    sys.exit(app.exec())
