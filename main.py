from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from translate import translate_
import sys


class Translator(QMainWindow):
    def __init__(self):
        super(Translator, self).__init__()
        loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.start)
        self.show()

    @pyqtSlot()
    def start(self):
        a = translate_(self.lineEdit.text(), self.comboBox.currentText())
        print(a)
        self.result.setText(str(a))


app = QApplication(sys.argv)
window = Translator()
try:
    sys.exit(app.exec_())
except:
    print('exit')
