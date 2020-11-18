import sys
from Gui import GrowthWindow, DCFWindow
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QDesktopWidget, QVBoxLayout, \
    QHBoxLayout, QLineEdit, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class SearchClass(QWidget):
    def __init__(self):
        super().__init__()  # initialzie super class
        self.width = 400
        self.height = 300
        self.iniUI()

    def iniUI(self):
        QToolTip.setFont(QFont("Times", 12, QFont.Black))
        self.setWindowTitle("Search Home")

        self.resize(self.width, self.height)

        # push button
        searchButton = QPushButton("Search", self)
        # searchButton.move(265, 87)
        searchButton.setToolTip("Search Ticker")

        # 输入
        labelTicker = QLabel("Enter Stock Ticker: ", self)
        entryTicker = QLineEdit(self)
        # 网格布局
        hlayout = QHBoxLayout(self)  # 水平布局
        hlayout.addWidget(labelTicker)
        hlayout.addWidget(entryTicker)
        hlayout.addWidget(searchButton)


        # connect 连接槽，也可以理解为方法
        searchButton.clicked.connect(lambda: self.search(str.upper(entryTicker.text())))

        '''
        need to figure out why editingFished() pass data twice.
        '''
        # entryTicker.editingFinished.connect(lambda: self.search(str.upper(entryTicker.text())))

        self.center()
        self.show()

    windowList = []
    def search(self, ticker):
        newScreen = GrowthWindow.GrowthWindow(ticker)
        self.windowList.append(newScreen)
        self.close()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 进程：管理所有窗口
    app.setWindowIcon(QIcon("/Users/shiyunqin/Desktop/Homework/Projects/估值模版/yfinance/API/Gui/image/icon2.png"))
    ex = SearchClass()
    app.exec_()  # 监听窗口事件
