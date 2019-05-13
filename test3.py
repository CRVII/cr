# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import PIL
import opensource
from opensource import *
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
from cp3 import *
import sys

class Ui_Dialog(QWidget):
    image1='2332'
    image2='rewr'
    color_percentage = 0
    def init(self):
        self.image1=''
        self.image2=''
        self.color_percentage=0
        self.tmd=0
        self.cp1=[]
        self.cp2=[]
        self.num=0
        self.ljc=''

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(742, 560)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 420, 81, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 420, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 420, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(460, 420, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 480, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 241, 301))
        #self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.setFixedSize(300,300)
        self.label_3.setStyleSheet("QLabel{background:White;}""QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(410, 70, 241, 301))
        #self.label_4.setText("")
        self.label_4.setFixedSize(300,300)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("QLabel{background:White;}""QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 480, 91, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText('返回')

        self.pushButton.clicked.connect(self.openfile)

        self.pushButton_2.clicked.connect(self.openfile2)
        self.pushButton_3.clicked.connect(self.histogram_color)
        self.pushButton_3.clicked.connect(self.aHash)
        self.pushButton_3.clicked.connect(self.judge)
        self.pushButton_3.clicked.connect(self.pp)
        #self.pushButton_3.clicked.connect(self.trans)
        #self.cc=cp3()
        #self.pushButton_5.clicked.connect(QCoreApplication.instance().exit)
        self.pushButton_3.clicked.connect(self.msg)
    #    self.openfile()
      #  self.openfile2()
        #self.pp()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def pp(self):
        print( self.color_percentage)
        print(self.tmd)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "请选择图片1"))
        self.pushButton.setText(_translate("Dialog", "浏览"))
        self.pushButton_2.setText(_translate("Dialog", "浏览"))
        self.label_2.setText(_translate("Dialog", "请选择图片2"))
        self.pushButton_3.setText(_translate("Dialog", "查看结果"))




    def openfile(self):
        img,openfile_name=QFileDialog.getOpenFileName(self,'选择文件',r'C:\Users\Inconceivable\Desktop\SamplePics','Image files(*.jpg)')
        self.image1 = img
        jpg=QtGui.QPixmap(img).scaled(self.label_3.width(),self.label_3.height())
        self.label_3.setPixmap(jpg)
        self.image1 = Image.open(img)
        #print(self.image1)

    def openfile2(self):
        img2,openfile_name2 = QFileDialog.getOpenFileName(self, '选择文件', r'C:\Users\Inconceivable\Desktop\SamplePics','Image files(*.jpg)')
        jpg2= QtGui.QPixmap(img2).scaled(self.label_4.width(), self.label_4.height())
        self.label_4.setPixmap(jpg2)
        self.image2=img2
        self.image2 = Image.open(img2)

   # print(image2)

    def histogram_color(self):
        size = (256, 256)
        self.image1 = self.image1.resize(size).convert('RGB')
        g = self.image1.histogram()
        self.image2 = self.image2.resize(size).convert('RGB')
        s = self.image2.histogram()
        assert len(g) == len(s), 'error'

        data = []

        for index in range(0, len(g)):
            if g[index] != s[index]:
                data.append(1 - abs(g[index] - s[index]) / max(g[index], s[index]))
            else:
                data.append(1)

        self.color_percentage=sum(data) / len(g)

    cp1=[]
    cp2=[]
    def getInfo1(self):
        size=(8,8)
        pixel = []
        for x in range(0, size[0]):
            for y in range(0, size[1]):
                pixel_value = self.image1.getpixel((x, y))
                pixel.append(pixel_value)

        average = sum(pixel) / len(pixel)

        for ft in pixel:
            if ft > average:
                self.cp1.append(1)
            else:
                self.cp1.append(0)

    def getInfo2(self):
        size = (8, 8)
        pixel = []
        for x in range(0, size[0]):
            for y in range(0, size[1]):
                pixel_value = self.image2.getpixel((x, y))
                pixel.append(pixel_value)

        average = sum(pixel) / len(pixel)

        for ft in pixel:
            if ft > average:
                self.cp2.append(1)
            else:
                self.cp2.append(0)

    num=0
    def compInfo(self):
        for index in range(0, len(self.cp1)):
            if self.cp1[index] != self.cp2[index]:
                self.num += 1

    tmd=0
    def aHash(self):
        size = (8,8)
        limt = 25
        self.image1 = self.image1.resize(size).convert('L').filter(ImageFilter.BLUR)
        self.image1 = ImageOps.equalize(self.image1)
        self.getInfo1()
        self.image2 = self.image2.resize(size).convert('L').filter(ImageFilter.BLUR)
        self.image2 = ImageOps.equalize(self.image2)
        self.getInfo2()

        assert len(self.cp1) == len(self.cp2), 'error'
        self.compInfo()
        #print(self.num)
        #print(limt)
        self.tmd=((limt-self.num)*2+50)/100

    ljc=''
    def judge(self):
        if self.color_percentage > 0.7 and self.tmd >0.5:
            self.ljc='Similar'
        else:
            self.ljc='Not Similar'
    '''
    def trans(self):
        aa=self.color_percentage
        return aa
    '''
    def msg(self):
        reply=QMessageBox.information(self,"结果",'颜色相似度'+self.color_percentage.__str__()
                                      +'\n'+'纹理相似度'+self.tmd.__str__()+'\n'
                                      +'是否相似'+self.ljc)

if __name__=="__main__":
    import sys
    import opensource
    opensource.ccc=10
    print(opensource.ccc)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    


