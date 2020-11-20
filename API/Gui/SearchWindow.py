import sys
import Company as Com
import yfinance as yf
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
        self.entryTicker = QLineEdit(self)
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

        # 网格布局
        hlayout = QHBoxLayout(self)  # 水平布局
        hlayout.addWidget(labelTicker)
        hlayout.addWidget(self.entryTicker)
        hlayout.addWidget(searchButton)

        self.center()
        self.show()

        searchButton.clicked.connect(self.getTicker)
        # searchButton.clicked.connect(lambda: self.search(company))
        '''
        need to figure out why editingFished() pass data twice.
        '''
        # entryTicker.editingFinished.connect(lambda: self.search(str.upper(entryTicker.text())))

    windowList = []

    def getTicker(self):
        inputTicker = str.upper(self.entryTicker.text())
        if inputTicker is not None:
            try:
                searchTicker = yf.Ticker(inputTicker)
                company = Com.Company(searchTicker)
                self.search(company)
                # initialize Company data
                '''
                need to figure out why editingFished() pass data twice.
                '''
                # entryTicker.editingFinished.connect(lambda: self.search(str.upper(entryTicker.text())))
            except:
                QMessageBox.warning(self, 'Warning!!!', "Ticker {} can not be found".format(inputTicker))
        return None

    def search(self, ticker):
        if ticker.suggestModel == "DCF":
            newScreen = DCFWindow.DCFWindow(ticker)
        elif ticker.suggestModel == "GROWTH":
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
