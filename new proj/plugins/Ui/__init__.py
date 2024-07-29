import sys
sys.path.append("..\\..\\")

import hook
from plugins.Ui.ui import Ui_MainWindow
from plugins.Ui.ask_sql_ui import Ui_Ask
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QTranslator, QCoreApplication, Signal
from PySide6.QtWidgets import QMessageBox
import pathlib
import importlib

plugs = pathlib.Path(__file__).parent.parent

@hook.hookimpl
def makeaUi():
    return Ui()

class Ui(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)
        self.setupUi(self)
        self.trans = QTranslator()

    def trans_to(self, to:str):
        self.trans.load((pathlib.Path(__file__).parent/"i18n").resolve()._str+"\\"+to+".qm")
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)

    def enuk(self):
        self.trans_to("English_UK")

    def enus(self):
        self.trans_to("English_US")

    def zhhans(self):
        self.trans_to("zh_Hans_CN")

    def zhhant(self):
        self.trans_to("zh_Hant_CN")

    def plug_sql_ask(self):
        msage = QMessageBox.question(self, QCoreApplication.translate("MessageBox" ,"MySQL installation", None),
                                    QCoreApplication.translate("MessageBox", "Have you download the Mysql db?", None),
                                    buttons=QMessageBox.StandardButtons.Yes|QMessageBox.StandardButtons.No,
                                    defaultButton=QMessageBox.StandardButtons.Yes)
        if msage == QMessageBox.StandardButton.Yes:
            ask = Askmain()
            othr = importlib.import_module((plugs/"Ui_others.py").stem)
            ask.passname.connect(othr.true)
            ask.close()


class Askmain(QMainWindow, Ui_Ask):
    passname = Signal(str, str)
    def __init__(self, parent=None):
        super(Askmain, self).__init__(parent)
        self.setupUi(self)
        self.trans = QTranslator()
        self.pushButton.clicked.connect(self.read)

    def trans_to(self, to:str):
        self.trans.load((pathlib.Path(__file__).parent/"i18n").resolve()._str+"\\"+to+".qm")
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)

    def enuk(self):
        self.trans_to("English_UK")

    def enus(self):
        self.trans_to("English_US")

    def zhhans(self):
        self.trans_to("zh_Hans_CN")

    def zhhant(self):
        self.trans_to("zh_Hant_CN")

    def read(self):
        usrname = self.lineEdit.text()
        usrpasswd = self.lineEdit_2.text()
        self.passname.emit(usrname, usrpasswd)
