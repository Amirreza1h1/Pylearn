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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(492, 489)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-size: 26px;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #aaa;\n"
"    border-radius: 10px;\n"
"    min-width: 60px;\n"
"    min-height: 60px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d0d0d0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #aaa;\n"
"    border: 2px dashed #ccc;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_12 = QPushButton(self.centralwidget)
        self.btn_12.setObjectName(u"btn_12")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_12.sizePolicy().hasHeightForWidth())
        self.btn_12.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_12, 3, 4, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_9, 3, 0, 1, 1)

        self.btn_15 = QPushButton(self.centralwidget)
        self.btn_15.setObjectName(u"btn_15")
        sizePolicy.setHeightForWidth(self.btn_15.sizePolicy().hasHeightForWidth())
        self.btn_15.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_15, 4, 3, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_6, 2, 1, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_8, 2, 4, 1, 1)

        self.btn_16 = QPushButton(self.centralwidget)
        self.btn_16.setObjectName(u"btn_16")
        sizePolicy.setHeightForWidth(self.btn_16.sizePolicy().hasHeightForWidth())
        self.btn_16.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_16, 4, 4, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_7, 2, 3, 1, 1)

        self.btn_13 = QPushButton(self.centralwidget)
        self.btn_13.setObjectName(u"btn_13")
        sizePolicy.setHeightForWidth(self.btn_13.sizePolicy().hasHeightForWidth())
        self.btn_13.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_13, 4, 0, 1, 1)

        self.btn_11 = QPushButton(self.centralwidget)
        self.btn_11.setObjectName(u"btn_11")
        sizePolicy.setHeightForWidth(self.btn_11.sizePolicy().hasHeightForWidth())
        self.btn_11.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_11, 3, 3, 1, 1)

        self.btn_10 = QPushButton(self.centralwidget)
        self.btn_10.setObjectName(u"btn_10")
        sizePolicy.setHeightForWidth(self.btn_10.sizePolicy().hasHeightForWidth())
        self.btn_10.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_10, 3, 1, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_5, 2, 0, 1, 1)

        self.btn_14 = QPushButton(self.centralwidget)
        self.btn_14.setObjectName(u"btn_14")
        sizePolicy.setHeightForWidth(self.btn_14.sizePolicy().hasHeightForWidth())
        self.btn_14.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_14, 4, 1, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_1, 1, 0, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_2, 1, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_3, 1, 3, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_4, 1, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Puzzle 15", None))
        self.btn_12.setText("")
        self.btn_9.setText("")
        self.btn_15.setText("")
        self.btn_6.setText("")
        self.btn_8.setText("")
        self.btn_16.setText("")
        self.btn_7.setText("")
        self.btn_13.setText("")
        self.btn_11.setText("")
        self.btn_10.setText("")
        self.btn_5.setText("")
        self.btn_14.setText("")
        self.btn_1.setText("")
        self.btn_2.setText("")
        self.btn_3.setText("")
        self.btn_4.setText("")
    # retranslateUi

