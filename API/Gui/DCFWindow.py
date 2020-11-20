import sys
import Company as Com
import yfinance as yf
from Gui import GrowthWindow, SearchWindow
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QDesktopWidget, QVBoxLayout, \
    QHBoxLayout, QLineEdit, QGridLayout, QLabel, QFrame
from PyQt5.QtGui import QIcon, QFont
import PyQt5.Qt as Qt


class DCFWindow(QWidget):
    def __init__(self, inputTicker):
        super().__init__()  # initialzie super class
        self.ticker = inputTicker
        self.width = 400
        self.height = 300
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle("Discount Cash Flow")
        self.resize(self.width, self.height)

        lbl_ticker = QLabel("Company name: ")
        lbl_profit_margin = QLabel("Profit Margin: ")
        lbl_growth_rate = QLabel("Growth Rate: ")
        lbl_perpetual_growth = QLabel("Perpetual Growth: ")
        lbl_eps = QLabel("EPS: ")
        lbl_fairvalue = QLabel("Fair Value Today: ")
        lbl_shareprice = QLabel("Shareprice Today: ")

        le_ticker = QLabel(self)
        le_ticker.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_ticker.setLineWidth(2)
        le_ticker.setText(self.ticker.name)

        le_profit_margin = QLabel(self)
        le_profit_margin.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_profit_margin.setLineWidth(2)
        le_profit_margin.setText("{:.2f}%".format(self.ticker.avg_profit_margin * 100))

        le_growth_rate = QLabel(self)
        le_growth_rate.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_growth_rate.setLineWidth(2)
        le_growth_rate.setText("{:.2f}%".format(self.ticker.growth_rate * 100))

        le_perpetual_growth = QLabel(self)
        le_perpetual_growth.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_perpetual_growth.setLineWidth(2)
        le_perpetual_growth.setText("{:.2f}%".format(self.ticker._perpetual_growth_rate * 100))

        le_eps = QLabel(self)
        le_eps.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_eps.setLineWidth(2)
        le_eps.setText("$ {:.2f}".format(self.ticker.eps))

        le_fairvalue = QLabel(self)
        le_fairvalue.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_fairvalue.setLineWidth(2)
        le_fairvalue.setText("$ {:.2f}".format(self.ticker.fair_value_of_equity_DCF))

        le_shareprice = QLabel(self)
        le_shareprice.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        le_shareprice.setLineWidth(2)
        le_shareprice.setText("$ {:.2f}".format(self.ticker.todays_share_price))

        # report section
        grid = QGridLayout(self)
        grid.addWidget(lbl_ticker, 0, 0)
        grid.addWidget(le_ticker, 0, 1)
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

        # button section
        btn_back = QPushButton("Back", self)
        btn_back.setToolTip("Return to Home")
        btn_customize = QPushButton("Customize", self)
        btn_customize.setToolTip("customize")
        btn_swithMode = QPushButton("Swtich", self)
        btn_swithMode.setToolTip("Switch to Growth Model")

        hlayout = QHBoxLayout()  # 水平布局
        hlayout.addStretch(1)
        hlayout.addWidget(btn_back)
        hlayout.addWidget(btn_customize)
        hlayout.addWidget(btn_swithMode)
        hlayout.addStretch(1)
        hlayout.setSpacing(15)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addStretch(1)
        grid.addLayout(vlayout, 7, 1)

        # set button connection
        btn_swithMode.clicked.connect(self.switchWindow)
        btn_back.clicked.connect(self.backHome)

        # finalize ui
        self.center()
        self.show()

    # must initialize this list
    windowList = []

    def switchWindow(self):
        self.ticker.getSuggestedModel = 'GROWTH'
        newScreen = GrowthWindow.GrowthWindow(self.ticker)
        self.windowList.append(newScreen)
        self.close()

    def backHome(self):
        newScreen = SearchWindow.SearchClass()
        self.windowList.append(newScreen)
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
