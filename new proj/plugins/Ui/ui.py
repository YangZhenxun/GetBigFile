# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GetBigFile.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QScrollArea, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(306, 531)
        self.actionSearch_place = QAction(MainWindow)
        self.actionSearch_place.setObjectName(u"actionSearch_place")
        icon = QIcon(QIcon.fromTheme(u"folder-open"))
        self.actionSearch_place.setIcon(icon)
        self.actionEnglish_UK = QAction(MainWindow)
        self.actionEnglish_UK.setObjectName(u"actionEnglish_UK")
        self.actionEnglish_US = QAction(MainWindow)
        self.actionEnglish_US.setObjectName(u"actionEnglish_US")
        self.actionzh_Hans = QAction(MainWindow)
        self.actionzh_Hans.setObjectName(u"actionzh_Hans")
        self.actionzh_Hant = QAction(MainWindow)
        self.actionzh_Hant.setObjectName(u"actionzh_Hant")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon1 = QIcon(QIcon.fromTheme(u"help-browser"))
        self.actionHelp.setIcon(icon1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon(QIcon.fromTheme(u"help-about"))
        self.actionAbout.setIcon(icon2)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon3 = QIcon(QIcon.fromTheme(u"window-close"))
        self.actionQuit.setIcon(icon3)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        icon4 = QIcon(QIcon.fromTheme(u"emblem-synchronized"))
        self.actionUpdate.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.centralwidget)
        icon5 = QIcon(QIcon.fromTheme(u"folder"))
        self.comboBox_2.addItem(icon5, "")
        icon6 = QIcon(QIcon.fromTheme(u"document-new"))
        self.comboBox_2.addItem(icon6, "")
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AudioCard))
        self.comboBox_2.addItem(icon7, "")
        icon8 = QIcon(QIcon.fromTheme(u"emblem-photos"))
        self.comboBox_2.addItem(icon8, "")
        icon9 = QIcon(QIcon.fromTheme(u"media-optical"))
        self.comboBox_2.addItem(icon9, "")
        icon10 = QIcon(QIcon.fromTheme(u"applications-multimedia"))
        self.comboBox_2.addItem(icon10, "")
        icon11 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.comboBox_2.addItem(icon11, "")
        icon12 = QIcon(QIcon.fromTheme(u"dialog-question"))
        self.comboBox_2.addItem(icon12, "")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.centralwidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 286, 400))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidget_2 = QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.gridLayout_2.addWidget(self.listWidget_2, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea_2, 1, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 306, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        self.menuLanguage = QMenu(self.menuSetting)
        self.menuLanguage.setObjectName(u"menuLanguage")
        icon13 = QIcon(QIcon.fromTheme(u"accessories-character-map"))
        self.menuLanguage.setIcon(icon13)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSearch_place)
        self.menuSetting.addAction(self.menuLanguage.menuAction())
        self.menuSetting.addAction(self.actionUpdate)
        self.menuLanguage.addAction(self.actionEnglish_UK)
        self.menuLanguage.addAction(self.actionEnglish_US)
        self.menuLanguage.addAction(self.actionzh_Hans)
        self.menuLanguage.addAction(self.actionzh_Hant)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        self.actionEnglish_UK.triggered.connect(self.enuk)
        self.actionEnglish_US.triggered.connect(self.enus)
        self.actionzh_Hans.triggered.connect(self.zhhans)
        self.actionzh_Hant.triggered.connect(self.zhhant)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Get Big File", None))
        self.actionSearch_place.setText(QCoreApplication.translate("MainWindow", "Search place...", None))
        self.actionEnglish_UK.setText(QCoreApplication.translate("MainWindow", u"English(UK)", None))
        self.actionEnglish_US.setText(QCoreApplication.translate("MainWindow", u"English(US)", None))
        self.actionzh_Hans.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587\uff08\u7b80\u4f53\uff09 ", None))
        self.actionzh_Hant.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587\uff08\u7e41\u9ad4\uff09", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", "Help...", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", "About?", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", "Quit", None))
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", "Update", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "File size:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"KB", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"MB", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"GB", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"TB", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", "All Files", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", "Document", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", "Music", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", "Picture", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", "Video", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", "Media", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", "Application", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", "Others", None))

        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuSetting.setTitle(QCoreApplication.translate("MainWindow", "Setting", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", "Language", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))
    # retranslateUi

