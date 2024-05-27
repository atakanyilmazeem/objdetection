import sys
import tasarim # tasarim kodlarını dahil ediyoruz

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from tasarim import Ui_MainWindow # tasarim kodlarını dahil ediyoruz

 # kutuphaneleri dahil ediyoruz
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self) # tasarim penceresinin tanımlaması yapılıyor

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    win = Window()
    win.show()  # pencere calıstırılıyor
    sys.exit(app.exec())