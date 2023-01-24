import sys

import numpy as np
import pyqtgraph as pg
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QLineEdit

from data import correlation, api


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/untitled.ui', self)
        self.word1 = 'words'
        self.word2 = 'letters'
        self.enterWords.clicked.connect(self.get_word_one)
        self.enterWords_2.clicked.connect(self.get_word_two)
        self.getCorrelation.clicked.connect(self.correlation_data)
        self.getDividedPlots.clicked.connect(self.calculate_different)

    def get_word_one(self):
        word, ok = QInputDialog.getText(self, "Ввод слов",
                                        'Введите слово или фразу, статистику по которой хотите получить,'
                                        ' или же биржевое сокращение ЗАГЛАВНЫМИ буквами',
                                        QLineEdit.Normal)
        try:
            self.word1 = str(word)
            self.statusBar().showMessage(f'Ваши слова {self.word1} и {self.word2}')
            self.statusBar().setStyleSheet("background-color : green")
        except Exception as E:
            self.error(E)

    def get_word_two(self):
        word, ok = QInputDialog.getText(self, "Ввод слов",
                                        'Введите слово или фразу, статистику по которой хотите получить,'
                                        ' или же биржевое сокращение ЗАГЛАВНЫМИ буквами', QLineEdit.Normal)
        try:
            self.word2 = str(word)
            self.statusBar().showMessage(f'Ваши слова {self.word1} и {self.word2}')
            self.statusBar().setStyleSheet("background-color : green")
        except Exception as E:
            self.error(E)

    def correlation_data(self):
        try:
            arrx, arry = self.arrays_equal()
            self.label.clear()
            self.label.setText(
                f'{self.word1} {self.word2} коэфицент корреляции: {correlation.Pearson_correlation_coefficient(arrx, arry)}')
            pg.plot(arrx, arry, pen=None, symbol='o')
            self.statusBar().showMessage(f'Результаты по {self.word1} и {self.word2}')
            self.statusBar().setStyleSheet("background-color : green")
        except Exception as E:
            self.error(E)

    def calculate_different(self):
        try:
            arrx, arry = self.arrays_equal()
            pg.plot(arrx)
            pg.plot(arry)
            self.statusBar().showMessage(f'Графики по {self.word1} и {self.word2}')
            self.statusBar().setStyleSheet("background-color : green")
        except Exception as E:
            self.error(E)

    def arrays_equal(self):
        try:
            first = np.array(api.closing_price(self.word1))
            if first.size == 0:
                first = np.array(api.trend_request([self.word1]), dtype=float)
        except:
            first = np.array(api.trend_request([self.word1]), dtype=float)
        second = np.array(api.closing_price(self.word2))
        if second.size == 0:
            second = np.array(api.trend_request([self.word2]), dtype=float)
        if first.size > second.size:
            first = first[first.size - second.size:]
        if second.size > first.size:
            second = second[second.size - first.size:]
        return first, second

    def error(self, E):
        self.statusBar().showMessage(f'{E}')
        self.statusBar().setStyleSheet("background-color : red")


# нужно добавить функцию для раздельного вывода
# и что бы выводились значения в массивах


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = MyApp()
        ex.show()
        sys.exit(app.exec())
    except Exception:
        pass
