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
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(822, 571)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #d4f1f4;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #75e6da;\n"
"	border-radius: 50px;\n"
"    border: 3px solid #ccc;\n"
"    padding: 15px;\n"
"	font-size: 16px;\n"
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
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #189ab4;\n"
"    border: 1px solid #ccc;\n"
"    padding: 5px;\n"
"	font-size: 16px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.player_status = QLineEdit(self.centralwidget)
        self.player_status.setObjectName(u"player_status")
        sizePolicy.setHeightForWidth(self.player_status.sizePolicy().hasHeightForWidth())
        self.player_status.setSizePolicy(sizePolicy)
        self.player_status.setReadOnly(True)

        self.gridLayout.addWidget(self.player_status, 4, 0, 1, 1)

        self.rock = QPushButton(self.centralwidget)
        self.rock.setObjectName(u"rock")
        sizePolicy.setHeightForWidth(self.rock.sizePolicy().hasHeightForWidth())
        self.rock.setSizePolicy(sizePolicy)
        font1 = QFont()
        self.rock.setFont(font1)

        self.gridLayout.addWidget(self.rock, 4, 1, 1, 1)

        self.draw = QLineEdit(self.centralwidget)
        self.draw.setObjectName(u"draw")
        sizePolicy.setHeightForWidth(self.draw.sizePolicy().hasHeightForWidth())
        self.draw.setSizePolicy(sizePolicy)
        self.draw.setReadOnly(True)

        self.gridLayout.addWidget(self.draw, 2, 0, 1, 1)

        self.paper = QPushButton(self.centralwidget)
        self.paper.setObjectName(u"paper")
        sizePolicy.setHeightForWidth(self.paper.sizePolicy().hasHeightForWidth())
        self.paper.setSizePolicy(sizePolicy)
        self.paper.setFont(font1)

        self.gridLayout.addWidget(self.paper, 4, 2, 1, 1)

        self.scissors = QPushButton(self.centralwidget)
        self.scissors.setObjectName(u"scissors")
        sizePolicy.setHeightForWidth(self.scissors.sizePolicy().hasHeightForWidth())
        self.scissors.setSizePolicy(sizePolicy)
        self.scissors.setFont(font1)

        self.gridLayout.addWidget(self.scissors, 4, 3, 1, 1)

        self.cpu_status = QLineEdit(self.centralwidget)
        self.cpu_status.setObjectName(u"cpu_status")
        sizePolicy.setHeightForWidth(self.cpu_status.sizePolicy().hasHeightForWidth())
        self.cpu_status.setSizePolicy(sizePolicy)
        self.cpu_status.setReadOnly(True)

        self.gridLayout.addWidget(self.cpu_status, 0, 0, 1, 1)

        self.restart = QPushButton(self.centralwidget)
        self.restart.setObjectName(u"restart")
        sizePolicy.setHeightForWidth(self.restart.sizePolicy().hasHeightForWidth())
        self.restart.setSizePolicy(sizePolicy)
        self.restart.setFont(font1)

        self.gridLayout.addWidget(self.restart, 0, 3, 1, 1)

        self.result = QTextEdit(self.centralwidget)
        self.result.setObjectName(u"result")
        sizePolicy.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy)
        self.result.setReadOnly(True)

        self.gridLayout.addWidget(self.result, 2, 1, 1, 3)

        self.cpu_choice = QLineEdit(self.centralwidget)
        self.cpu_choice.setObjectName(u"cpu_choice")
        sizePolicy.setHeightForWidth(self.cpu_choice.sizePolicy().hasHeightForWidth())
        self.cpu_choice.setSizePolicy(sizePolicy)
        self.cpu_choice.setFont(font1)
        self.cpu_choice.setReadOnly(True)

        self.gridLayout.addWidget(self.cpu_choice, 0, 2, 1, 1)

        self.about = QPushButton(self.centralwidget)
        self.about.setObjectName(u"about")
        sizePolicy.setHeightForWidth(self.about.sizePolicy().hasHeightForWidth())
        self.about.setSizePolicy(sizePolicy)
        self.about.setFont(font1)

        self.gridLayout.addWidget(self.about, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.player_status.setText(QCoreApplication.translate("MainWindow", u"Player WINs", None))
        self.rock.setText(QCoreApplication.translate("MainWindow", u"Rock\ud83e\udea8", None))
        self.draw.setText(QCoreApplication.translate("MainWindow", u"Draws", None))
        self.paper.setText(QCoreApplication.translate("MainWindow", u"Paper\ud83d\udcc4", None))
        self.scissors.setText(QCoreApplication.translate("MainWindow", u"Scissors\u2702\ufe0f", None))
        self.cpu_status.setText(QCoreApplication.translate("MainWindow", u"CPU WINs", None))
        self.restart.setText(QCoreApplication.translate("MainWindow", u"RESTART!", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

