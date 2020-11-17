import sys
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
        app.setWindowIcon(QIcon("../image/icon.png"))

        self.resize(self.width, self.height)

        # push button
        searchButton = QPushButton("Search", self)
        # searchButton.move(265, 87)
        searchButton.setToolTip("Search Ticker")

        # 输入
        labelTicker = QLabel("Enter Stock Ticker: ", self)
        entryTicker = QLineEdit(self)

        # 网格布局
        #
        hlayout = QHBoxLayout(self)  # 水平布局
        # hlayout.addStretch(1)
        hlayout.addWidget(labelTicker)
        hlayout.addWidget(entryTicker)
        hlayout.addWidget(searchButton)
        # hlayout.addStretch(1)
        # hlayout.setSpacing(20)
        # self.setLayout(hlayout)


        # connect 连接槽，也可以理解为方法
        searchButton.clicked.connect(self.close)

        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # overload from self.close
    def closeEvent(self, event):
        result = QMessageBox.question(self, "Attention: ", "Search for ticker", QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.Yes)
        if result == QMessageBox.Yes:
            print(dir(event))
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 进程：管理所有窗口
    mc = SearchClass()
    app.exec_()  # 监听窗口事件
