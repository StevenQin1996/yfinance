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

        lbl_ticker = QLabel("Ticker: ")
        lbl_profit_margin = QLabel("Profit Margin: ")
        lbl_growth_rate = QLabel("Growth Rate: ")
        lbl_perpetual_growth = QLabel("Perpetual Growth: ")
        lbl_eps = QLabel("EPS: ")
        lbl_fairvalue = QLabel("Fair Value Today: ")
        lbl_shareprice = QLabel("Shareprice Today: ")

        le_profit_margin = QLabel(self)
        le_profit_margin.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_profit_margin.setLineWidth(2)
        le_profit_margin.setText("placeholder")

        le_ticker = QLabel(self)
        le_ticker.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_ticker.setLineWidth(2)
        le_ticker.setText("placeholder")

        le_growth_rate = QLabel(self)
        le_growth_rate.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_ticker.setLineWidth(2)
        le_growth_rate.setText("placeholder")

        le_perpetual_growth = QLabel(self)
        le_perpetual_growth.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_perpetual_growth.setLineWidth(2)
        le_perpetual_growth.setText("placeholder")

        le_eps = QLabel(self)
        le_eps.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_eps.setLineWidth(2)
        le_eps.setText("placeholder")

        le_fairvalue = QLabel(self)
        le_fairvalue.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_fairvalue.setLineWidth(2)
        le_fairvalue.setText("placeholder")

        le_shareprice = QLabel(self)
        le_shareprice.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_shareprice.setLineWidth(2)
        le_shareprice.setText("placeholder")

        grid=QGridLayout(self)
        grid.addWidget(lbl_ticker,0,0)
        grid.addWidget(le_ticker,0,1)
        grid.addWidget(lbl_profit_margin, 1, 0)
        grid.addWidget(le_profit_margin, 1, 1)
        grid.addWidget(lbl_growth_rate, 2, 0)
        grid.addWidget(le_growth_rate, 2, 1)
        grid.addWidget(lbl_perpetual_growth, 3, 0)
        grid.addWidget(le_perpetual_growth, 3, 1)
        grid.addWidget(lbl_eps, 4, 0)
        grid.addWidget(le_eps, 4, 1)
        grid.addWidget(lbl_fairvalue, 5, 0)
        grid.addWidget(le_fairvalue, 5, 1)
        grid.addWidget(lbl_shareprice, 6, 0)
        grid.addWidget(le_shareprice, 6, 1)



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
        hlayout.setSpacing(15)

        # vlayout = QVBoxLayout(self)
        # vlayout.addStretch(1)
        # vlayout.addLayout(hlayout)
        # vlayout.addStretch(1)

        grid.addLayout(hlayout,7,0)




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

