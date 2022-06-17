from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.Qt3DCore import *

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('calform.ui', None)
        self.ui.show()

        self.ui.buttunnum0.clicked.connect(partial(self.nums,"0"))
        self.ui.buttunnum1.clicked.connect(partial(self.nums,"1"))
        self.ui.buttunnum2.clicked.connect(partial(self.nums,"2"))
        self.ui.buttunnum3.clicked.connect(partial(self.nums,"3"))
        self.ui.buttunnum4.clicked.connect(partial(self.nums,"4"))
        self.ui.buttunnum5.clicked.connect(partial(self.nums,"5"))
        self.ui.buttunnum6.clicked.connect(partial(self.nums,"6"))
        self.ui.buttunnum7.clicked.connect(partial(self.nums,"7"))
        self.ui.buttunnum8.clicked.connect(partial(self.nums,"8"))
        self.ui.buttunnum9.clicked.connect(partial(self.nums,"9"))

        self.ui.cbuttun.clicked.connect(self.c)
        self.ui.prcbuttun.clicked.connect(self.prc)
        self.ui.divisionbuttun.clicked.connect(self.division)
        self.ui.mulbuttun.clicked.connect(self.mul)
        self.ui.minbuttun.clicked.connect(self.minus)
        self.ui.sumbuttun.clicked.connect(self.sum)
        self.ui.dotbuttun.clicked.connect(self.dot)
        self.ui.enterbuttun.clicked.connect(self.equal)
    
    def nums(self, Number):
        self.ui.text.setText(self.ui.text.toPlainText() + Number)
    
    def c(self):
        self.ui.text.setText("")

    def prc(self):
        self.placeholder = "%"
        self.num1 = float(self.ui.text.toPlainText())
        self.ui.text.setText("")
        self.ui.text.setText(str(self.num1 / 100))

    def division(self):
        self.placeholder = "/"
        self.num1 = float(self.ui.text.toPlainText())
        self.ui.text.setText("")
    
    def mul(self):
        self.placeholder = "x"
        self.num1 = float(self.ui.text.toPlainText())
        self.ui.text.setText("")
    
    def minus(self):
        self.placeholder = "-"
        self.num1 = float(self.ui.text.toPlainText())
        self.ui.text.setText("")

    def sum(self):
        self.placeholder = "+"
        self.num1 = float(self.ui.text.toPlainText())
        self.ui.text.setText("")

    def dot(self):
        if "." in self.ui.text.toPlainText():
            self.ui.text.setText(self.ui.text.toPlainText() + "you already have .")
        else:
            self.ui.text.setText(self.ui.text.toPlainText() + ".")

    def equal(self):

        if self.placeholder == "/":
            self.num2 = float(self.ui.text.toPlainText())
            if self.num2 == 0:
                self.ui.text.setText("Divided by zero")
            else:
                self.ui.text.setText(str(self.num1 / self.num2))

        if self.placeholder == "x":
            self.num2 = float(self.ui.text.toPlainText())
            self.ui.text.setText(str(self.num1 * self.num2))
        
        if self.placeholder == "-":
            self.num2 = float(self.ui.text.toPlainText())
            self.ui.text.setText(str(self.num1 - self.num2))

        if self.placeholder == "+":
            self.num2 = float(self.ui.text.toPlainText())
            self.ui.text.setText(str(self.num1 + self.num2))


calculator1 = QApplication([])
window = Calculator()
calculator1.exec()