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
        MainWindow.resize(493, 405)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #999999;\n"
"}\n"
"\n"
"/* Central widget */\n"
"centralwidget {\n"
"    padding: 20px;\n"
"}\n"
"\n"
"/* Text edits */\n"
"QTextEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Line edits */\n"
"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Push buttons */\n"
"QPushButton {\n"
"    background-color: #007bff;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 20px;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* About button */\n"
"#about {\n"
"    background-color: #ffc107;\n"
"    color: black;\n"
""
                        "    margin-top: 10px;\n"
"}\n"
"\n"
"#about:hover {\n"
"    background-color: #baa107;\n"
"}\n"
"\n"
"/* Result text edit */\n"
"#result {\n"
"    background-color: #f8f9fa;\n"
"    border: 1px solid #dee2e6;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"    max-height: 200px;\n"
"}\n"
"\n"
"/* Turn counter */\n"
"#turns_number {\n"
"    background-color: #e9ecef;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Win counters */\n"
"#cpu1_win, #cpu2_win, #user_win {\n"
"    background-color: #e9ecef;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cpu2_win = QLineEdit(self.centralwidget)
        self.cpu2_win.setObjectName(u"cpu2_win")
        self.cpu2_win.setReadOnly(True)

        self.gridLayout.addWidget(self.cpu2_win, 3, 0, 1, 1)

        self.user_win = QLineEdit(self.centralwidget)
        self.user_win.setObjectName(u"user_win")

        self.gridLayout.addWidget(self.user_win, 6, 1, 1, 2)

        self.result = QTextEdit(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setReadOnly(True)

        self.gridLayout.addWidget(self.result, 4, 0, 1, 4)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_2, 2, 0, 1, 1)

        self.cpu1_win = QLineEdit(self.centralwidget)
        self.cpu1_win.setObjectName(u"cpu1_win")
        self.cpu1_win.setReadOnly(True)

        self.gridLayout.addWidget(self.cpu1_win, 3, 3, 1, 1)

        self.turns_number = QLineEdit(self.centralwidget)
        self.turns_number.setObjectName(u"turns_number")
        self.turns_number.setReadOnly(True)

        self.gridLayout.addWidget(self.turns_number, 1, 1, 1, 2)

        self.user = QTextEdit(self.centralwidget)
        self.user.setObjectName(u"user")
        self.user.setReadOnly(True)

        self.gridLayout.addWidget(self.user, 5, 1, 1, 2)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 2, 3, 1, 1)

        self.about = QPushButton(self.centralwidget)
        self.about.setObjectName(u"about")

        self.gridLayout.addWidget(self.about, 0, 1, 1, 2)

        self.ro = QPushButton(self.centralwidget)
        self.ro.setObjectName(u"ro")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ro.sizePolicy().hasHeightForWidth())
        self.ro.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.ro, 7, 2, 2, 2)

        self.posht = QPushButton(self.centralwidget)
        self.posht.setObjectName(u"posht")
        sizePolicy.setHeightForWidth(self.posht.sizePolicy().hasHeightForWidth())
        self.posht.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.posht, 7, 0, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"game", None))
        self.cpu2_win.setText(QCoreApplication.translate("MainWindow", u"Wins: ", None))
        self.user_win.setText(QCoreApplication.translate("MainWindow", u"Wins: ", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:16pt;\">CPU 2</span></p></body></html>", None))
        self.cpu1_win.setText(QCoreApplication.translate("MainWindow", u"Wins: ", None))
        self.turns_number.setText(QCoreApplication.translate("MainWindow", u"Round: 1", None))
        self.user.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:16pt;\">YOU</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:16pt;\">CPU 1</span></p></body></html>", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.ro.setText("✋on hand")
        self.posht.setText("back of hand🤚")
    # retranslateUi

