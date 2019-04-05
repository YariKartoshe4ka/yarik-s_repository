"""

    Creator: Yaroslav Kikel
    Finished: 31st March 2019 year 


"""
import sys
# Импортируем наш интерфейс из файла
from calc import *
from PyQt5 import QtCore, QtGui, QtWidgets
from math import pi, e

num1 = 0
num2 = 0

plus = False
minus = False
umn = False
delete = False
stepen = False

error = False

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.pushButton.clicked.connect(self.MyFunction) #btn 1
        self.ui.pushButton_2.clicked.connect(self.MyFunction_2) #btn 2
        self.ui.pushButton_3.clicked.connect(self.MyFunction_3) #btn 3
        self.ui.pushButton_4.clicked.connect(self.MyFunction_4) #btn 4
        self.ui.pushButton_5.clicked.connect(self.MyFunction_5) #btn 5
        self.ui.pushButton_6.clicked.connect(self.MyFunction_6) #btn 6
        self.ui.pushButton_7.clicked.connect(self.MyFunction_7) #btn 7
        self.ui.pushButton_8.clicked.connect(self.MyFunction_8) #btn 8
        self.ui.pushButton_9.clicked.connect(self.MyFunction_9) #btn 9
        self.ui.pushButton_10.clicked.connect(self.MyFunction_10) #btn /
        self.ui.pushButton_16.clicked.connect(self.MyFunction_16) #btn =
        self.ui.pushButton_11.clicked.connect(self.MyFunction_11) #btn *
        self.ui.pushButton_12.clicked.connect(self.MyFunction_12) #btn -
        self.ui.pushButton_13.clicked.connect(self.MyFunction_13) #btn 0
        self.ui.pushButton_14.clicked.connect(self.MyFunction_14) #btn 00
        self.ui.pushButton_15.clicked.connect(self.MyFunction_15) #btn .
        self.ui.pushButton_17.clicked.connect(self.MyFunction_17) #btn PI
        self.ui.pushButton_18.clicked.connect(self.MyFunction_18) #btn E
        self.ui.pushButton_19.clicked.connect(self.MyFunction_19) #btn ^
        self.ui.pushButton_20.clicked.connect(self.MyFunction_20) #btn +
        self.ui.pushButton_21.clicked.connect(self.MyFunction_21) #btn C
        self.ui.pushButton_22.clicked.connect(self.MyFunction_22) #btn +/-

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку                  
    def MyFunction(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "1"
        self.ui.textEdit.setText(num1)

    def MyFunction_2(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "2"
        self.ui.textEdit.setText(num1)

    def MyFunction_3(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "3"
        self.ui.textEdit.setText(num1)

    def MyFunction_4(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "4"
        self.ui.textEdit.setText(num1)

    def MyFunction_5(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "5"
        self.ui.textEdit.setText(num1)

    def MyFunction_6(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "6"
        self.ui.textEdit.setText(num1)

    def MyFunction_7(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "7"
        self.ui.textEdit.setText(num1)

    def MyFunction_8(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "8"
        self.ui.textEdit.setText(num1)

    def MyFunction_9(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "9"
        self.ui.textEdit.setText(num1)

    def MyFunction_13(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "0"
        self.ui.textEdit.setText(num1)

    def MyFunction_14(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "00"
        self.ui.textEdit.setText(num1)

    def MyFunction_15(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = self.ui.textEdit.toPlainText() + "."
        self.ui.textEdit.setText(num1)

    def MyFunction_10(self):
        global delete
        delete = True
        global num2
        num2 = self.ui.textEdit.toPlainText()
        global num1
        num1 = 0
        self.ui.textEdit.setText("")

    def MyFunction_11(self):
        global umn
        umn = True
        global num2
        num2 = self.ui.textEdit.toPlainText()
        global num1
        num1 = 0
        self.ui.textEdit.setText("")

    def MyFunction_12(self):
        global minus
        minus = True
        global num2
        num2 = self.ui.textEdit.toPlainText()
        global num1
        num1 = 0
        self.ui.textEdit.setText("")

    def MyFunction_17(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = ""
        self.ui.textEdit.setText("")
        self.ui.textEdit.setText(str(pi))

    def MyFunction_18(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        global num1
        num1 = ""
        self.ui.textEdit.setText("")
        self.ui.textEdit.setText(str(e))

    def MyFunction_22(self):
        if error:
            self.ui.textEdit.setText('')
            global error
            error = False
        numtest = self.ui.textEdit.toPlainText()
        global num1
        num1 = int(numtest) - (int(numtest) * 2)
        self.ui.textEdit.setText(str(num1))

    def MyFunction_19(self):
        global stepen
        stepen = True
        global num2
        num2 = self.ui.textEdit.toPlainText()
        global num1
        num1 = ""
        self.ui.textEdit.setText("")
        
    def MyFunction_20(self):
        global plus
        plus = True
        global num2
        num2 = self.ui.textEdit.toPlainText()
        global num1
        num1 = ""
        self.ui.textEdit.setText("")

    def MyFunction_21(self):
        global num1
        num1 = ""
        self.ui.textEdit.setText("")

    def MyFunction_16(self):
        if delete:
            try:
                float(num2) / float(num1)
            except:
                self.ui.textEdit.setText('Error')
                global error
                error = True
                global delete
                delete = False
            else:
                rez = float(num2) / float(num1)
                self.ui.textEdit.setText(str(rez))
                global delete
                delete = False
        elif umn:
            try:
                float(num2) * float(num1)
            except:
                self.ui.textEdit.setText('Error')
                global error
                error = True
                global umn
                umn = False
            else:
                rez = float(num2) * float(num1)
                self.ui.textEdit.setText(str(rez))
                global umn
                umn = False
        elif minus:
            try:
                float(num2) - float(num1)
            except:
                self.ui.textEdit.setText('Error')
                global error
                error = True
                global minus
                minus = False
            else:
                rez = float(num2) - float(num1)
                self.ui.textEdit.setText(str(rez))
                global minus
                minus = False
        elif plus:
            try:
                float(num2) + float(num1)
            except:
                self.ui.textEdit.setText('Error')
                global error
                error = True
                global plus
                plus = False
            else:
                rez = float(num2) + float(num1)
                self.ui.textEdit.setText(str(rez))
                global plus
                plus = False
        elif stepen:
            try:
                float(num2) ** float(num1)
            except:
                self.ui.textEdit.setText('Error')
                global error
                error = True
                global stepen
                stepen = False
            else:
                rez = float(num2) ** float(num1)
                self.ui.textEdit.setText(str(rez))
                global stepen
                stepen = False
        
if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
