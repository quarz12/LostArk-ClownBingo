# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from functools import partial
from random import sample
from typing import List, Tuple

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.arr=[[],[],[],[],[]]
        self.bar:List[QtWidgets.QFrame]=[]
        self.bar_count=5
        self.bingo=False
        self.turn=0
        self.buttons:List[QtWidgets.QPushButton]=None
        self.bingos:List[str]=[]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 700))
        MainWindow.setMaximumSize(QtCore.QSize(700, 700))
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(180, 160, 60, 60))
        self.b1.setText("")
        self.b1.setObjectName("b1")
        self.arr[0].append(self.b1)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(250, 160, 60, 60))
        self.b2.setText("")
        self.b2.setObjectName("b2")
        self.arr[0].append(self.b2)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(320, 160, 60, 60))
        self.b3.setText("")
        self.b3.setObjectName("b3")
        self.arr[0].append(self.b3)
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(390, 160, 60, 60))
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.arr[0].append(self.b4)
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(460, 160, 60, 60))
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.arr[0].append(self.b5)
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(180, 230, 60, 60))
        self.b6.setText("")
        self.b6.setObjectName("b6")
        self.arr[1].append(self.b6)
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(250, 230, 60, 60))
        self.b7.setText("")
        self.b7.setObjectName("b7")
        self.arr[1].append(self.b7)
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(320, 230, 60, 60))
        self.b8.setText("")
        self.b8.setObjectName("b8")
        self.arr[1].append(self.b8)
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(390, 230, 60, 60))
        self.b9.setText("")
        self.b9.setObjectName("b9")
        self.arr[1].append(self.b9)
        self.b10 = QtWidgets.QPushButton(self.centralwidget)
        self.b10.setGeometry(QtCore.QRect(460, 230, 60, 60))
        self.b10.setText("")
        self.b10.setObjectName("b10")
        self.arr[1].append(self.b10)
        self.b11 = QtWidgets.QPushButton(self.centralwidget)
        self.b11.setGeometry(QtCore.QRect(180, 300, 60, 60))
        self.b11.setText("")
        self.b11.setObjectName("b11")
        self.arr[2].append(self.b11)
        self.b12 = QtWidgets.QPushButton(self.centralwidget)
        self.b12.setGeometry(QtCore.QRect(250, 300, 60, 60))
        self.b12.setText("")
        self.b12.setObjectName("b12")
        self.arr[2].append(self.b12)
        self.b13 = QtWidgets.QPushButton(self.centralwidget)
        self.b13.setGeometry(QtCore.QRect(320, 300, 60, 60))
        self.b13.setText("")
        self.b13.setObjectName("b13")
        self.arr[2].append(self.b13)
        self.b14 = QtWidgets.QPushButton(self.centralwidget)
        self.b14.setGeometry(QtCore.QRect(390, 300, 60, 60))
        self.b14.setText("")
        self.b14.setObjectName("b14")
        self.arr[2].append(self.b14)
        self.b15 = QtWidgets.QPushButton(self.centralwidget)
        self.b15.setGeometry(QtCore.QRect(460, 300, 60, 60))
        self.b15.setText("")
        self.b15.setObjectName("b15")
        self.arr[2].append(self.b15)
        self.b16 = QtWidgets.QPushButton(self.centralwidget)
        self.b16.setGeometry(QtCore.QRect(180, 370, 60, 60))
        self.b16.setText("")
        self.b16.setObjectName("b16")
        self.arr[3].append(self.b16)
        self.b17 = QtWidgets.QPushButton(self.centralwidget)
        self.b17.setGeometry(QtCore.QRect(250, 370, 60, 60))
        self.b17.setText("")
        self.b17.setObjectName("b17")
        self.arr[3].append(self.b17)
        self.b18 = QtWidgets.QPushButton(self.centralwidget)
        self.b18.setGeometry(QtCore.QRect(320, 370, 60, 60))
        self.b18.setText("")
        self.b18.setObjectName("b18")
        self.arr[3].append(self.b18)
        self.b19 = QtWidgets.QPushButton(self.centralwidget)
        self.b19.setGeometry(QtCore.QRect(390, 370, 60, 60))
        self.b19.setText("")
        self.b19.setObjectName("b19")
        self.arr[3].append(self.b19)
        self.b20 = QtWidgets.QPushButton(self.centralwidget)
        self.b20.setGeometry(QtCore.QRect(460, 370, 60, 60))
        self.b20.setText("")
        self.b20.setObjectName("b20")
        self.arr[3].append(self.b20)
        self.b21 = QtWidgets.QPushButton(self.centralwidget)
        self.b21.setGeometry(QtCore.QRect(180, 440, 60, 60))
        self.b21.setText("")
        self.b21.setObjectName("b21")
        self.arr[4].append(self.b21)
        self.b22 = QtWidgets.QPushButton(self.centralwidget)
        self.b22.setGeometry(QtCore.QRect(250, 440, 60, 60))
        self.b22.setText("")
        self.b22.setObjectName("b22")
        self.arr[4].append(self.b22)
        self.b23 = QtWidgets.QPushButton(self.centralwidget)
        self.b23.setGeometry(QtCore.QRect(320, 440, 60, 60))
        self.b23.setText("")
        self.b23.setObjectName("b23")
        self.arr[4].append(self.b23)
        self.b24 = QtWidgets.QPushButton(self.centralwidget)
        self.b24.setGeometry(QtCore.QRect(390, 440, 60, 60))
        self.b24.setText("")
        self.b24.setObjectName("b24")
        self.arr[4].append(self.b24)
        self.b25 = QtWidgets.QPushButton(self.centralwidget)
        self.b25.setGeometry(QtCore.QRect(460, 440, 60, 60))
        self.b25.setAutoFillBackground(True)
        self.b25.setText("")
        self.b25.setObjectName("b25")
        self.arr[4].append(self.b25)


        for i,x in enumerate(self.arr):
            for j,y in enumerate(x):
                setattr(y,"grid",(i,j))

        self.buttons=[item for y in self.arr for item in y]
        for button in self.buttons:
            button.clicked.connect(partial(self.mkturn,button))

        #select 2 random buttons to flip
        for btn in sample(self.buttons,2):
            self.flip(btn)


        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setEnabled(True)
        self.reset.setGeometry(QtCore.QRect(250, 550, 200, 50))
        self.reset.setObjectName("reset")

        self.reset.clicked.connect(partial(self.reset_,MainWindow))
        self.hp1 = QtWidgets.QFrame(self.centralwidget)
        self.hp1.setGeometry(QtCore.QRect(145, 60, 60, 50))
        self.hp1.setAutoFillBackground(False)
        self.hp1.setStyleSheet("background-color: red;")
        self.hp1.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.hp1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hp1.setLineWidth(1)
        self.hp1.setMidLineWidth(0)
        self.hp1.setObjectName("hp1")
        self.bar.append(self.hp1)
        self.hp2 = QtWidgets.QFrame(self.centralwidget)
        self.hp2.setGeometry(QtCore.QRect(215, 60, 60, 50))
        self.hp2.setAutoFillBackground(False)
        self.hp2.setStyleSheet("background-color: red;")
        self.hp2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.hp2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hp2.setLineWidth(1)
        self.hp2.setMidLineWidth(0)
        self.hp2.setObjectName("hp2")
        self.bar.append(self.hp2)
        self.hp3 = QtWidgets.QFrame(self.centralwidget)
        self.hp3.setGeometry(QtCore.QRect(285, 60, 60, 50))
        self.hp3.setAutoFillBackground(False)
        self.hp3.setStyleSheet("background-color: red;")
        self.hp3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.hp3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hp3.setLineWidth(1)
        self.hp3.setMidLineWidth(0)
        self.hp3.setObjectName("hp3")
        self.bar.append(self.hp3)
        self.hp4 = QtWidgets.QFrame(self.centralwidget)
        self.hp4.setGeometry(QtCore.QRect(355, 60, 60, 50))
        self.hp4.setAutoFillBackground(False)
        self.hp4.setStyleSheet("background-color: red;")
        self.hp4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.hp4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hp4.setLineWidth(1)
        self.hp4.setMidLineWidth(0)
        self.hp4.setObjectName("hp4")
        self.bar.append(self.hp4)
        self.hp6 = QtWidgets.QFrame(self.centralwidget)
        self.hp5 = QtWidgets.QFrame(self.centralwidget)
        self.hp5.setGeometry(QtCore.QRect(425, 60, 60, 50))
        self.hp5.setAutoFillBackground(False)
        self.hp5.setStyleSheet("background-color: red;")
        self.hp5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.hp5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hp5.setLineWidth(1)
        self.hp5.setMidLineWidth(0)
        self.hp5.setObjectName("hp5")
        self.bar.append(self.hp5)
        self.hp6.setGeometry(QtCore.QRect(495, 60, 60, 50))
        self.hp6.setAutoFillBackground(False)
        self.hp6.setStyleSheet("background-color: red;")
        self.hp6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.hp6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hp6.setLineWidth(1)
        self.hp6.setMidLineWidth(0)
        self.hp6.setObjectName("hp6")
        self.bar.append(self.hp6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def reset_(self,main):
        ui=Ui_MainWindow()
        ui.setupUi(main)

    def get_radius(self,btn:QtWidgets.QPushButton)->List[Tuple[int,int]]:
        list_= [btn.grid]
        if not btn.grid[0]==4:
            list_.append((btn.grid[0]+1,btn.grid[1]))
        if not btn.grid[0] == 0:
            list_.append((btn.grid[0] - 1, btn.grid[1]))
        if not btn.grid[1]==4:
            list_.append((btn.grid[0],btn.grid[1]+1))
        if not btn.grid[1]==0:
            list_.append((btn.grid[0],btn.grid[1]-1))
        return list_

    def check_bingo(self): #TODO only new ones keep a list of completed bingos
        for i,line in enumerate(self.arr):
            if all([self.is_red(btn)for btn in line]):
                if not (string:=f"line{i}") in self.bingos:
                    self.bingos.append(string)
                    for btn in line:
                        self.lock(btn)
                    self.bingo=True

        for i in range(5):
            list_=[]
            for j in range(5):
                list_.append(self.arr[j][i])
            if all([self.is_red(btn) for btn in list_]):
                if not (string := f"column{i}") in self.bingos:
                    self.bingos.append(string)
                    for btn in list_:
                        self.lock(btn)
                    self.bingo=True

    def mkturn(self,btn:QtWidgets.QPushButton):
        for b in self.get_radius(btn):
            self.flip(self.arr[b[0]][b[1]])
        self.end_turn()

    def end_turn(self):
        self.turn+=1
        if self.turn>3:
            self.turn=1

        self.check_bingo()
        if self.turn==3:
            if self.bingo:
                self.turn_bar()
            else:
                self.end_game(False)
        if all([self.is_red(btn) for btn in self.buttons]):
            self.end_game(False)
        self.bingo=False
        if self.won():
            self.end_game(True)

    def won(self):
        return all([x.styleSheet() == "background-color: none;" for x in self.bar])

    def end_game(self,success:bool):
        for btn in self.buttons:
            btn.blockSignals(True)
        result=QtWidgets.QLabel(self.centralwidget)
        result.setText("YOU WON" if success else "YOU LOST")
        result.setGeometry(QtCore.QRect(150, 250, 400, 100))
        result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        result.setStyleSheet("background:darkred;" if not success else "background:yellow;")
        result.show()

    def turn_bar(self):
        self.bar[self.bar_count].setStyleSheet("background-color: none;")
        self.bar_count-=1

    def is_red(self,button:QtWidgets.QPushButton):
        return button.styleSheet()=='QPushButton {background-color: red;}' or button.styleSheet()=='QPushButton {background-color: darkred;}'

    def flip(self,button:QtWidgets.QPushButton):
        if button.styleSheet() !='QPushButton {background-color: darkred;}':
            if button.styleSheet() != 'QPushButton {background-color: red;}':
                button.setStyleSheet('QPushButton {background-color: red;}')
            else:
                button.setStyleSheet('QPushButton {background-color: none;}')

    def lock(self,button:QtWidgets.QPushButton):
        button.setStyleSheet('QPushButton {background-color: darkred;}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.reset.setText(_translate("MainWindow", "Reset"))


if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)  #init widget
    MainWindow.show()
    sys.exit(app.exec())