# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(322, 331)
        MainWindow.setStyleSheet(u" QWidget {\n"
"            background-color: #222222;\n"
"        }\n"
"\n"
"QPushButton {\n"
"            background-color: #3498db;\n"
"            color: white;\n"
"            border-radius: 5px;\n"
"            padding: 10px 20px;\n"
"            font-weight: bold;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"            background-color: #2980b9;\n"
"        }\n"
"        \n"
"        QLineEdit {\n"
"            background-color: #f1c40f;\n"
"            color: black;\n"
"            border-style: solid;\n"
"            border-width: 1px;\n"
"            border-color: #e74c3c;\n"
"            padding: 5px;\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"        }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.restart = QPushButton(self.centralwidget)
        self.restart.setObjectName(u"restart")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restart.sizePolicy().hasHeightForWidth())
        self.restart.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.restart, 0, 2, 1, 1)

        self.about = QPushButton(self.centralwidget)
        self.about.setObjectName(u"about")
        sizePolicy.setHeightForWidth(self.about.sizePolicy().hasHeightForWidth())
        self.about.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.about, 0, 0, 1, 1)

        self.counter = QLineEdit(self.centralwidget)
        self.counter.setObjectName(u"counter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.counter.sizePolicy().hasHeightForWidth())
        self.counter.setSizePolicy(sizePolicy1)
        self.counter.setReadOnly(True)

        self.gridLayout.addWidget(self.counter, 3, 1, 1, 1)

        self.user_guess = QLineEdit(self.centralwidget)
        self.user_guess.setObjectName(u"user_guess")
        sizePolicy1.setHeightForWidth(self.user_guess.sizePolicy().hasHeightForWidth())
        self.user_guess.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.user_guess, 1, 1, 1, 1)

        self.guess = QPushButton(self.centralwidget)
        self.guess.setObjectName(u"guess")
        sizePolicy.setHeightForWidth(self.guess.sizePolicy().hasHeightForWidth())
        self.guess.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.guess, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"game", None))
        self.restart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.guess.setText(QCoreApplication.translate("MainWindow", u"TRY YOUR GUESS", None))
    # retranslateUi

