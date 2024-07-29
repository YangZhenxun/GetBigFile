# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ask_sql.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_Ask(object):
    def setupUi(self, Ask):
        if not Ask.objectName():
            Ask.setObjectName(u"Ask")
        Ask.resize(313, 197)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        Ask.setWindowIcon(icon)
        Ask.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.centralwidget = QWidget(Ask)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        Ask.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Ask)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 313, 33))
        Ask.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Ask)
        self.statusbar.setObjectName(u"statusbar")
        Ask.setStatusBar(self.statusbar)

        self.retranslateUi(Ask)

        QMetaObject.connectSlotsByName(Ask)
    # setupUi

    def retranslateUi(self, Ask):
        Ask.setWindowTitle(QCoreApplication.translate("Ask", "MySQL user infomation", None))
        self.label.setText(QCoreApplication.translate("Ask", "Please input your MySQL username:", None))
        self.label_2.setText(QCoreApplication.translate("Ask", "Please input your MySQL password:", None))
        self.pushButton.setText(QCoreApplication.translate("Ask", "Sure", None))
    # retranslateUi

