from PyQt5.QtWidgets import QApplication, QDialog
from processFunks import *
from loading import Ui_LoadWindow
from PyQt5.QtGui import QIcon
from m import Ui_MainWindow
from PyQt5 import QtCore
import sys


class LoadWindow(QDialog, Ui_LoadWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check)

    def check(self):
        self.accept()  # Закрытие окна


class MainWindow(QDialog, Ui_MainWindow):
    def __init__(self, ):
        super().__init__()

        self.setupUi(self)
        self.messages = 0
        self.dop = 0
        self.anim1 = NumsGenForAnim()
        self.anim1.my_sig.connect(self.run_anim1)
        self.timer = False
        self.send.clicked.connect(
            lambda: self.anim1.start() if self.message.text().strip() else None
        )  # Если сообщение не пустое

    def music_time(self, num):
        self.time.setText(num)
        if num == 'Ещё?':
            self.click()

    def send_message(self, text):
        self.blue_message(text_progress(text))
        res = return_answer(text)  # Обработка естественного языка
        if 'music' in res:
            self.check(401)
            for i in [self.author, self.name, self.time, self.labelG, self.pause, self.verticalSlider]:
                i.show()
            self.set_data(get_music(get_genre(text)))
            self.click()
            if self.n == 1:
                self.click()
            self.messages = 200
            self.musicTimer = MusicTime(self.time.text())
            self.musicTimer.my_sig.connect(self.music_time)
            self.musicTimer.start()
            self.timer = True

        elif 'weather' in res:
            res = res.split('!')
            self.check(401)
            t, p = get_weather(int(res[1]), res[2])
            self.set_weather(p)
            self.about_weather.setText(t)
            self.messages = 150
            self.weather.setText(res[2])
            self.weather_label.show()
            self.about_weather.show()
            self.weather.show()
        else:
            # Отрисовка сообщения пользователя
            self.red_message(text_progress(res))  # Отрисовка сообщения ассистента

    def red_message(self, data):
        def pro(lab):
            lab.setText(text)
            lab.setGeometry(QtCore.QRect(20, (80 + self.messages), width, height))
            lab.show()

        text, width, height = data
        height += self.dop
        self.check(height)
        if self.labl0red.text() == '!':
            pro(self.labl0red)
        elif self.labl1red.text() == '!':
            pro(self.labl1red)
        elif self.labl2red.text() == '!':
            pro(self.labl2red)
        elif self.labl3red.text() == '!':
            pro(self.labl3red)
        self.messages = height + self.messages + 10
        self.dop = 0

    def blue_message(self, data):
        def pro(lab):
            lab.setText(text)
            lab.setGeometry(QtCore.QRect(int(220 - width + 110), (80 + self.messages), width, height))
            lab.show()

        text, width, height = data
        self.check(height)
        if self.labl0blu.text() == '!':
            pro(self.labl0blu)
        elif self.labl1blu.text() == '!':
            pro(self.labl1blu)
        elif self.labl2blu.text() == '!':
            pro(self.labl2blu)
        elif self.labl3blu.text() == '!':
            pro(self.labl3blu)
        elif self.labl4blu.text() == '!':
            pro(self.labl4blu)
        self.messages = height + self.messages + 10

    def check(self, height):
        if self.messages + height > 450:
            for i in [self.labl0red, self.labl1red, self.labl2red, self.labl3red,
                      self.labl0blu, self.labl1blu, self.labl2blu, self.labl3blu, self.labl4blu]:
                i.hide()
                i.setText('!')
                self.messages = 0
            for i in [self.author, self.name, self.time, self.labelG, self.pause, self.verticalSlider,
                      self.about_weather, self.weather_label, self.weather]:
                i.hide()
            self.media_player.stop()
            if self.timer:
                self.musicTimer.disconnect()

    def run_anim1(self, num):  # Анимация кнопки
        if num[1]:
            if num[0] == '1':
                print(self.message.text())
                self.send_message(self.message.text())
                self.message.setText('')
                self.message.setEnabled(False)
            self.send.setIcon(QIcon(f'res/send1/{num[0]}.jpg'))
        else:
            self.send.setIcon(QIcon(f'res/send2/{num[0]}.jpg'))
            if num[0] == '19':
                self.message.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoadWindow()
    if not login.exec_():  # Проверка что окно не закрыто по нажатию на крестик
        sys.exit(-1)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
