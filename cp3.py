# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cp3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import opensource

import test3
#from test3 import *
import opensource
from opensource import *

class Ui_Dialog1(object):
    c_p=0
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(356, 282)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 61, 16))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(120, 50, 151, 21))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 54, 12))
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(120, 120, 151, 21))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(120, 186, 151, 20))
        self.textBrowser_3.setObjectName("textBrowser_3")

        uu=test3.Ui_Dialog()
        self.c_p=uu.trans()
        print(self.c_p)
        self.textBrowser_2.setText(self.c_p.__str__())

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "颜色相似度"))
        self.label_2.setText(_translate("Dialog", "纹理相似度"))
        self.label_3.setText(_translate("Dialog", "是否相似"))


    def setT(self,aa):
        self.c_p=aa
        print(self.c_p)


if __name__=="__main__":
    import sys
    opensource.ccc=10
    print(opensource.ccc)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
