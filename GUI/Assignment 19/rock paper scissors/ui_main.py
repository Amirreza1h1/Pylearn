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
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(431, 483)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #d4f1f4;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #75e6da;\n"
"	border-radius: 50px;\n"
"    border: 3px solid #ccc;\n"
"    padding: 15px;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #05445e;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px 15px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0000ff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cpu_win = QLineEdit(self.centralwidget)
        self.cpu_win.setObjectName(u"cpu_win")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpu_win.sizePolicy().hasHeightForWidth())
        self.cpu_win.setSizePolicy(sizePolicy)
        self.cpu_win.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cpu_win.setReadOnly(True)

        self.gridLayout.addWidget(self.cpu_win, 0, 4, 1, 1)

        self.user_choice = QLineEdit(self.centralwidget)
        self.user_choice.setObjectName(u"user_choice")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.user_choice.sizePolicy().hasHeightForWidth())
        self.user_choice.setSizePolicy(sizePolicy1)
        self.user_choice.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.user_choice.setReadOnly(True)

        self.gridLayout.addWidget(self.user_choice, 2, 2, 1, 1)

        self.scissors = QPushButton(self.centralwidget)
        self.scissors.setObjectName(u"scissors")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scissors.sizePolicy().hasHeightForWidth())
        self.scissors.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.scissors, 3, 4, 1, 1)

        self.restart = QPushButton(self.centralwidget)
        self.restart.setObjectName(u"restart")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.restart.sizePolicy().hasHeightForWidth())
        self.restart.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.restart, 1, 0, 1, 1)

        self.cpu_choice = QLineEdit(self.centralwidget)
        self.cpu_choice.setObjectName(u"cpu_choice")
        sizePolicy1.setHeightForWidth(self.cpu_choice.sizePolicy().hasHeightForWidth())
        self.cpu_choice.setSizePolicy(sizePolicy1)
        self.cpu_choice.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cpu_choice.setReadOnly(True)

        self.gridLayout.addWidget(self.cpu_choice, 1, 2, 1, 1)

        self.paper = QPushButton(self.centralwidget)
        self.paper.setObjectName(u"paper")
        sizePolicy2.setHeightForWidth(self.paper.sizePolicy().hasHeightForWidth())
        self.paper.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.paper, 3, 2, 1, 1)

        self.rock = QPushButton(self.centralwidget)
        self.rock.setObjectName(u"rock")
        sizePolicy2.setHeightForWidth(self.rock.sizePolicy().hasHeightForWidth())
        self.rock.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.rock, 3, 0, 1, 1)

        self.user_win = QLineEdit(self.centralwidget)
        self.user_win.setObjectName(u"user_win")
        sizePolicy.setHeightForWidth(self.user_win.sizePolicy().hasHeightForWidth())
        self.user_win.setSizePolicy(sizePolicy)
        self.user_win.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.user_win.setReadOnly(True)

        self.gridLayout.addWidget(self.user_win, 0, 0, 1, 1)

        self.about = QPushButton(self.centralwidget)
        self.about.setObjectName(u"about")
        sizePolicy2.setHeightForWidth(self.about.sizePolicy().hasHeightForWidth())
        self.about.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.about, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.scissors.setText(QCoreApplication.translate("MainWindow", u"Scissors", None))
        self.restart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.paper.setText(QCoreApplication.translate("MainWindow", u"Paper", None))
        self.rock.setText(QCoreApplication.translate("MainWindow", u"Rock", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

