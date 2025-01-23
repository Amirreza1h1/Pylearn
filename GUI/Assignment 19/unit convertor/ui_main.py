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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(601, 531)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                              stop: 0 #a33178, stop: 1 #9942b4);\n"
"}\n"
"QPushButton {\n"
"	border: 2px solid #8f8f91;\n"
"	border-radius: 6px;\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                              stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"	min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                              stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:default {\n"
"	border-color: navy;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 4px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QLineEdit[readOnly=\"true\"] {\n"
"	background-color: #e0e0e0;\n"
"	color: #666;\n"
"}\n"
"\n"
"QGridLayout {\n"
"	spacing: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Type_box = QComboBox(self.centralwidget)
        self.Type_box.addItem("")
        self.Type_box.addItem("")
        self.Type_box.addItem("")
        self.Type_box.addItem("")
        self.Type_box.setObjectName(u"Type_box")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Type_box.sizePolicy().hasHeightForWidth())
        self.Type_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Type_box, 1, 0, 1, 3)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_6.setStyleSheet(u"")
        self.lineEdit_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_6.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_6, 0, 0, 1, 3)

        self.From_box = QComboBox(self.centralwidget)
        self.From_box.setObjectName(u"From_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.From_box.sizePolicy().hasHeightForWidth())
        self.From_box.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.From_box, 4, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy2)
        self.lineEdit_5.setStyleSheet(u"")
        self.lineEdit_5.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.lineEdit_5.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_3.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_3, 3, 0, 1, 1)

        self.To_output = QLineEdit(self.centralwidget)
        self.To_output.setObjectName(u"To_output")
        self.To_output.setReadOnly(True)

        self.gridLayout.addWidget(self.To_output, 6, 2, 1, 1)

        self.To_box = QComboBox(self.centralwidget)
        self.To_box.setObjectName(u"To_box")
        sizePolicy1.setHeightForWidth(self.To_box.sizePolicy().hasHeightForWidth())
        self.To_box.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.To_box, 4, 2, 1, 1)

        self.From_input = QLineEdit(self.centralwidget)
        self.From_input.setObjectName(u"From_input")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.From_input.sizePolicy().hasHeightForWidth())
        self.From_input.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.From_input, 6, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_3, 7, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Unit Convertor", None))
        self.Type_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Mass", None))
        self.Type_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Length", None))
        self.Type_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.Type_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Digital volume", None))

        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"Convertor", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Equal", None))
    # retranslateUi

