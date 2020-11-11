import sys

form PyQt5.QWidgets import  QApplications, QMainWindow
from window import *

if __name__ == '__main__':

    app = QApplications(sys.argv)

    mainWindows = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.show()
    sys.exit(app.exec_())

