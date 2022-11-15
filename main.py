import sys

from PyQt5 import uic
from PyQt5.Qt import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QMessageBox, QLineEdit, QLabel
from pyqtgraph import PlotWidget
import pyqtgraph as pg

import numpy as np

import api
import correlation


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.word1 = 'words'
        self.word2 = 'letters'
        self.pushButton.clicked.connect(self.get_word)
        self.pushButton_3.clicked.connect(self.calculate)

    def get_word(self):
        word, ok = QInputDialog.getText(self, "Ввод слов",
                                        "Фразы(разделены символом ~), статистика по которой будет получена:", QLineEdit.Normal)
        self.word1, self.word2 = str(word).split('~') if ok else None

    def calculate(self):
        arrx = np.array(api.trend_request([self.word1]), dtype=float)
        arry = np.array(api.trend_request([self.word2]), dtype=float)
        self.label.clear()
        self.label.setText(f'{self.word1} {self.word2} коэфицент корреляции: {correlation.Pearson_correlation_coefficient(arrx,arry)}')
        pg.plot(arrx, arry, pen=None, symbol='o')


    def plot(self, arrX, arrY):
        self.graphWidget.plot(arrX, arrY)

    # def get_words(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())
