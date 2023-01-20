import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QLineEdit
import pyqtgraph as pg

import numpy as np

from data import correlation, api


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/untitled.ui', self)
        self.word1 = 'words'
        self.word2 = 'letters'
        self.enterWords.clicked.connect(self.get_word)
        self.getCorrelation.clicked.connect(self.correlation_data)
        self.getDividedPlots.clicked.connect(self.calculate_different)

    def get_word(self):
        word, ok = QInputDialog.getText(self, "Ввод слов",
                                        "Фразы(разделены символом ~), статистика по которой будет получена:",
                                        QLineEdit.Normal)
        try:
            self.word1, self.word2 = str(word).split('~') if ok else None
            self.statusBar().showMessage(f'Ваши слова {self.word1} и {self.word2}')
            self.statusBar().setStyleSheet("background-color : green")
        except ValueError:
            self.statusBar().showMessage('Вы ввели мало слов, попробуйте еще раз')
            self.statusBar().setStyleSheet("background-color : red")
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
        return np.array(api.trend_request([self.word1]), dtype=float), np.array(api.trend_request([self.word2]),
                                                                                dtype=float)

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
