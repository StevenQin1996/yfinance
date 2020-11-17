import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QDesktopWidget, QVBoxLayout, \
    QHBoxLayout, QLineEdit, QGridLayout, QLabel, QFrame
from PyQt5.QtGui import QIcon, QFont
import PyQt5.Qt as Qt

class DCFWindow(QWidget):
    def __init__(self):
        super().__init__()  # initialzie super class
        self.width = 400
        self.height = 300
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle("Discount Cash Flow")
        self.resize(self.width, self.height)

        hlayout = QHBoxLayout(self)  # 水平布局

        btn_back = QPushButton("Back", self)
        btn_back.setToolTip("Return to Home")
        hlayout.addWidget(btn_back)

        btn_customize = QPushButton("Customize", self)
        btn_customize.setToolTip("customize")
        hlayout.addWidget(btn_customize)

        btn_swithMode = QPushButton("Swtich", self)
        btn_swithMode.setToolTip("Switch to Growth Model")
        hlayout.addWidget(btn_swithMode)

        hlayout.setSpacing(10)






        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 进程：管理所有窗口
    mc = DCFWindow()
    app.exec_()  # 监听窗口事件

