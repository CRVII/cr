import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from cp3 import *
from test3 import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化主窗口
    main = QDialog()
    main_ui = Ui_Dialog()
    main_ui.setupUi(main)
    # 实例化子窗口
    child = QDialog()
    child_ui = Ui_Dialog1()
    child_ui.setupUi(child)

    # 按钮绑定事件
    btn = main_ui.pushButton_3
    btn.clicked.connect(child.show)

    # 显示
    main.show()
    sys.exit(app.exec_())