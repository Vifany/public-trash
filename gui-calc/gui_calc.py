# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import sys
import ui_MainForm
import ctypes



FDIC = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        'X': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '=': lambda a, b: a
         }

reg1 = float(0.0)
reg2 = float(0.0)
func = '='
funcflag = True

def clr():
    global reg1
    global reg2
    text = ui.text_main.toPlainText()
    if text == '0.0' or text == '0':
        reg1 = 0.0
        reg2 = 0.0
    ui.text_main.setPlainText('0')
    return

def calculate(fun):
    global func
    global reg1
    global reg2
    global funcflag
    reg2 = float(ui.text_main.toPlainText())
    reg1 = FDIC[func](reg1, reg2)
    ui.text_main.setPlainText(str(reg1))
    reg1 = reg2
    reg2 = 0
    func = fun
    funcflag = True
    return

def addsym(sym):
    global funcflag
    line= str(ui.text_main.toPlainText())
    if line == '0' or line == '0.0' or funcflag == True:
        line = ''
        funcflag = False
    line=line + str(sym)
    ui.text_main.setPlainText(line)


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui =ui_MainForm.Ui_MainWindow()
ui.setupUi(window)

ui.button_1.clicked.connect(lambda:addsym('1'))
ui.button_2.clicked.connect(lambda:addsym('2'))
ui.button_3.clicked.connect(lambda:addsym('3'))
ui.button_4.clicked.connect(lambda:addsym('4'))
ui.button_5.clicked.connect(lambda:addsym('5'))
ui.button_6.clicked.connect(lambda:addsym('6'))
ui.button_7.clicked.connect(lambda:addsym('7'))
ui.button_8.clicked.connect(lambda:addsym('8'))
ui.button_9.clicked.connect(lambda:addsym('9'))
ui.button_zero.clicked.connect(lambda:addsym('0'))
ui.button_float.clicked.connect(lambda:addsym('.'))


ui.button_add.clicked.connect(lambda:calculate('+'))
ui.button_mul.clicked.connect(lambda:calculate('X'))
ui.button_div.clicked.connect(lambda:calculate('/'))
ui.button_sub.clicked.connect(lambda:calculate('-'))
ui.button_clr.clicked.connect(lambda:clr())
ui.button_ret.clicked.connect(lambda:calculate('='))

window.show()

sys.exit(app.exec_())