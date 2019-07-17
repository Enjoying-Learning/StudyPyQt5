import sys
from ui import Ui_MainWindow  # 调用ui模块中的Ui_MainWindow()类
from PyQt5 import QtWidgets
# Qt设计师上第一步创建时选择了Main Window时选择QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
# Qt设计师上第一步创建时选择了Dialog时选择QDialog
# Qt设计师上第一步创建时选择了Widget时选择QWidget


class Digcalculator(QMainWindow, Ui_MainWindow):  # 继承自父类QtWidgets.QMainWindow
    # Qt设计师上第一步创建时选择了Main Window时选择QMainWindow
    # Qt设计师上第一步创建时选择了Dialog时选择QDialog
    # Qt设计师上第一步创建时选择了Widget时选择QWidget

    # 定义5个类变量，公用变量
    lcdstring = ''  # 用来显示lcd上用来显示的字符
    operation = ''  # 定义一个操作符
    currentNum = 0  # 当前值
    previousNum = 0  # 上一个值
    result = 0  # 存放结果

    # parent = None代表此QWidget属于最上层的窗口,也就是MainWindows.
    def __init__(self, parent=None):
        super(Digcalculator, self).__init__()  # 因为继承关系，要对父类初始化
        # 通过super初始化父类，__init__()函数无self，若直接QtWidgets.QDialog).__init__(self)，括号里是有self的
        self.setupUi(self)
        self.action()  # 存放所有的信号槽

    def action(self):
        # 定义按下数字执行的方法
        self.button_0.clicked.connect(self.buttonClicked)
        self.button_1.clicked.connect(self.buttonClicked)
        self.button_2.clicked.connect(self.buttonClicked)
        self.button_3.clicked.connect(self.buttonClicked)
        self.button_4.clicked.connect(self.buttonClicked)
        self.button_5.clicked.connect(self.buttonClicked)
        self.button_6.clicked.connect(self.buttonClicked)
        self.button_7.clicked.connect(self.buttonClicked)
        self.button_8.clicked.connect(self.buttonClicked)
        self.button_9.clicked.connect(self.buttonClicked)
        self.button_point.clicked.connect(self.buttonClicked)

        # 定义按下操作符执行的方法
        self.button_plus.clicked.connect(self.opClicked)
        self.button_subtract.clicked.connect(self.opClicked)  # -
        self.button_multiply.clicked.connect(self.opClicked)  # *
        self.button_divide.clicked.connect(self.opClicked)  # /

        # 定义按下清除键执行的方法
        self.button_clear.clicked.connect(self.clearClicked)

        # 定义按下等于号执行的方法
        self.button_equal.clicked.connect(self.equalClicked)

    def buttonClicked(self):
        if len(self.lcdstring) <= 27:  # 当lcd数值显示长度小于等于27时执行
            self.lcdstring = self.lcdstring + self.sender().text()
            # 新lcd的显示内容=老lcd的显示内容+按钮传过来的对象的text值
            if str(self.lcdstring) == '.':  # 若第一次输入时为1个点
                self.lcdstring = '0.'  # 我们把'.'替换成'0.'
                self.lcd.display(self.lcdstring)
                # 将self.lcdstring值在lcd中显示出来
                self.currentNum = float(self.lcdstring)
                # 将lcd中的数字强制转换为浮点型，方便小数计算
            else:
                if str(self.lcdstring).count('.') > 1:  # 当小数点的数量大于1时,必须转换成str字符串，否则无count属性
                    self.lcdstring = str(self.lcdstring)[:-1]  # 我们利用切片将最后一个点去除
                    self.lcd.display(self.lcdstring)
                    # 将self.lcdstring值在lcd中显示出来
                    self.currentNum = float(self.lcdstring)  # 无法将字符串转换为浮点型
                    # 将lcd中的数字强制转换为浮点型，方便小数计算
                else:
                    self.lcd.display(self.lcdstring)
                    # 将self.lcdstring值在lcd中显示出来
                    self.currentNum = float(self.lcdstring)  # 无法将字符串转换为浮点型
                    # 将lcd中的数字强制转换为浮点型，方便小数计算
        else:  # lcd长度大于9
            pass

    def opClicked(self):
        # 按下等号后都要,清空操作符，为后续判断是否是连续运算做准备(比如9 * 9 * 9 = 729，但若不判断是否是连续运算程序则只运算等号前一步运算即9 * 9 = 81)
        if self.operation != '':  # 操作符不是空的，证明是连续运算
            self.equalClicked()
            self.previousNum = self.currentNum  # 将当前值传送给previousNum变量
            self.currentNum = 0  # 并把当前值清零
            self.lcdstring = ''  # 按下操作符后lcd显示屏首先会被清空
            self.operation = self.sender().text()  # 操作符等于按钮传过来的对象的text值
        else:
            self.previousNum = self.currentNum  # 将当前值传送给previousNum变量
            self.currentNum = 0  # 并把当前值清零
            self.lcdstring = ''  # 按下操作符后lcd显示屏首先会被清空
            self.operation = self.sender().text()  # 操作符等于按钮传过来的对象的text值
        # print(self.sender().text())
        # print(self.sender().objectName())

    def clearClicked(self):
        # 清除键按下去就是把所有参数清零就好
        self.lcdstring = ''  # 用来显示lcd上用来显示的字符
        self.operation = ''  # 定义一个操作符
        self.currentNum = 0  # 当前值
        self.previousNum = 0  # 上一个值
        self.result = 0  # 存放结果
        self.lcd.display(0)  # 最后把lcd中的数字改成0

    def equalClicked(self):
        if self.operation == '+':  # 当操作符为加号
            self.result = self.previousNum+self.currentNum  # 结果就是上一个值加当前值
            self.lcd.display(self.result)  # 把结果显示在lcd中

        if self.operation == '-':  # 当操作符为减号
            self.result = self.previousNum-self.currentNum  # 结果就是上一个值减当前值
            self.lcd.display(self.result)  # 把结果显示在lcd中

        if self.operation == '*':  # 当操作符为乘号
            self.result = self.previousNum*self.currentNum  # 结果就是上一个值乘当前值
            self.lcd.display(self.result)  # 把结果显示在lcd中

        if self.operation == '/':  # 当操作符为除以号
            if self.currentNum == 0:
                self.lcd.display('Error')
                self.result = 0  # 出现错误后将结果清零
                self.previousNum = 0  # 上一个值清零
            else:
                self.result = self.previousNum/self.currentNum  # 结果就是上一个值除当前值
                self.lcd.display(self.result)  # 把结果显示在lcd中

        # 将运算的结果result顺便保存到currentNum当前值里,为后续计算做准备.否则无法准确计算紧接着操作.
        self.currentNum = self.result
        self.lcdstring = ''  # 将lcdstring顺便清空,为后续计算做准备.否则无法准确计算紧接着操作.相当于初始化
        # 清空操作符，为后续判断是否是连续运算做准备(比如9*9*9=729，但若不判断是否是连续运算程序则只运算等号前一步运算即9*9=81)
        self.operation = ''

    def closeEvent(self, event):  # 函数名固定不可变
        # 当我们关闭一个窗口时，在PyQt中就会触发一个QCloseEvent的事件，正常情况下会直接关闭这个窗口，
        # 但是我们不希望这样的事情发生，所以我们需要重新定义QCloseEvent，函数名称为closeEvent不可变
        reply = QtWidgets.QMessageBox.question(self, u'警告', u'确认退出?', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        # QtWidgets.QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()  # 关闭窗口
        else:
            event.ignore()  # 忽视点击X事件


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Digcalculator()
    window.show()
    sys.exit(app.exec_())