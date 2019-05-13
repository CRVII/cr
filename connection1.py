import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from test1 import *
from test3 import *
from cp3 import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化主窗口
    main = QMainWindow()
    main_ui = Ui_MainWindow()
    main_ui.setupUi(main)
    # 实例化子窗口
    child = QDialog()
    child_ui = Ui_Dialog()
    child_ui.setupUi(child)

   # a=child_ui.trans()
    '''
    def chuanzhi():
        child_ui1.c_p = child_ui.color_percentage
        '''
    # 按钮绑定事件
    btn = main_ui.pushButton
    btn.clicked.connect(child.show)
    btn.clicked.connect(main.close)
    btn.clicked.connect(child_ui.init)

    '''
    child1 = QDialog()
    child_ui1 = Ui_Dialog1()
    child_ui1.setupUi(child1)
    #child_ui1.setT(a)
    
    
    btn1=child_ui.pushButton_3
    btn1.clicked.connect(child1.show)
    #btn1.clicked.connect(chuanzhi)
    '''
    btn2=child_ui.pushButton_5
    btn2.clicked.connect(main.show)
    btn2.clicked.connect(child.close)

    # 显示
    main.show()
    sys.exit(app.exec_())