# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from time import sleep


class NumsGenForAnim(QtCore.QThread):
    my_sig = QtCore.pyqtSignal(bool)

    def run(self):
        sleep(11.5)
        self.my_sig.emit(True)


class Ui_LoadWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(363, 603)
        MainWindow.setFixedSize(363, 603)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#f8faff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 450, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#f8faff;\n"
                                      "border-radius: 20px;\n"
                                      "color: #f8faff;")
        self.pushButton.setObjectName("pushButton")
        # self.pushButton.setEnabled(False) КЛИКАБЕЛЬНОСТЬ В МОМЕНТ ЗАГРУЗКИ
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 301, 261))
        self.label.setStyleSheet("background-color:#f8faff;")
        self.label.setText("")
        self.label.setObjectName("label")
        gif = QtGui.QMovie('res/loading.gif')
        self.label.setMovie(gif)
        gif.start()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 400, 281, 21))
        self.label_2.setStyleSheet("background-color:#f8faff;")
        self.label_2.setText("")
        self.label_2.setObjectName("label")
        gif2 = QtGui.QMovie('res/loadingMessages.gif')
        self.label_2.setMovie(gif2)
        gif2.start()
        self.anim = NumsGenForAnim()
        self.anim.my_sig.connect(self.stop_gif)
        self.anim.start()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сергей"))
        MainWindow.setWindowIcon(QIcon('res/LOGO.jpg'))
        self.pushButton.setText(_translate("MainWindow", "Готово"))

    def stop_gif(self, bool):
        if bool:
            self.pushButton.setStyleSheet("background-color:#2864fe;\n"
                                          "border-radius: 20px;\n"
                                          "color: #f8faff;")
            self.label_2.setPixmap(QPixmap('res/loadingMessages.jpg'))
            self.pushButton.setEnabled(True)
