# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(427, 547)
        MainWindow.setStyleSheet(u"/* Main Window */\n"
"MainWindow {\n"
"    background-color: #F0F0F0;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Central Widget */\n"
"centralwidget {\n"
"    padding: 20px;\n"
"}\n"
"\n"
"/* Layouts */\n"
"QVBoxLayout {\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QGridLayout {\n"
"    column-gap: 10px;\n"
"    row-gap: 10px;\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Line Edit */\n"
"QLineEdit {\n"
"    font-size: 16px;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"\n"
"/* Text Edit */\n"
"QTextEdit {\n"
"    font-family: Consolas, monospace;\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"\n"
"/* Push Button */\n"
"QPushButton {\n"
"    font-size: 16px;\n"
"    padding: 10px 15px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"    background-color: #007bff;\n"
"    color: white;\n"
"}\n"
""
                        "\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Grid Layout Items */\n"
"QLabel {\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"/* Checkbox */\n"
"QCheckBox {\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Status Label */\n"
"status_label {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    color: green;\n"
"}\n"
"\n"
"/* Priority Label */\n"
"priority_label {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    color: orange;\n"
"}\n"
"\n"
"/* Delete Button */\n"
"QPushButton#add_btn {\n"
"    background-color: #dc3545;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#add_btn:hover {\n"
"    background-color: #bd2130;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.GL_tasks = QGridLayout()
        self.GL_tasks.setObjectName(u"GL_tasks")
        self.d_label = QLabel(self.centralwidget)
        self.d_label.setObjectName(u"d_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_label.sizePolicy().hasHeightForWidth())
        self.d_label.setSizePolicy(sizePolicy)
        self.d_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.GL_tasks.addWidget(self.d_label, 0, 3, 1, 1)

        self.p_label = QLabel(self.centralwidget)
        self.p_label.setObjectName(u"p_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.p_label.sizePolicy().hasHeightForWidth())
        self.p_label.setSizePolicy(sizePolicy1)
        self.p_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.GL_tasks.addWidget(self.p_label, 0, 2, 1, 1)

        self.is_done_label = QLabel(self.centralwidget)
        self.is_done_label.setObjectName(u"is_done_label")
        sizePolicy.setHeightForWidth(self.is_done_label.sizePolicy().hasHeightForWidth())
        self.is_done_label.setSizePolicy(sizePolicy)
        self.is_done_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.is_done_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.GL_tasks.addWidget(self.is_done_label, 0, 0, 1, 1)

        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.GL_tasks.addWidget(self.title_label, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.GL_tasks)

        self.GL_new_task = QGridLayout()
        self.GL_new_task.setObjectName(u"GL_new_task")
        self.new_title = QLineEdit(self.centralwidget)
        self.new_title.setObjectName(u"new_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.new_title.sizePolicy().hasHeightForWidth())
        self.new_title.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.new_title.setFont(font)

        self.GL_new_task.addWidget(self.new_title, 0, 1, 1, 1)

        self.new_description = QTextEdit(self.centralwidget)
        self.new_description.setObjectName(u"new_description")
        sizePolicy.setHeightForWidth(self.new_description.sizePolicy().hasHeightForWidth())
        self.new_description.setSizePolicy(sizePolicy)

        self.GL_new_task.addWidget(self.new_description, 1, 1, 1, 1)

        self.new_time = QLineEdit(self.centralwidget)
        self.new_time.setObjectName(u"new_time")

        self.GL_new_task.addWidget(self.new_time, 1, 3, 1, 1)

        self.new_date = QLineEdit(self.centralwidget)
        self.new_date.setObjectName(u"new_date")

        self.GL_new_task.addWidget(self.new_date, 1, 4, 1, 1)

        self.add_btn = QPushButton(self.centralwidget)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setBold(True)
        font1.setKerning(True)
        self.add_btn.setFont(font1)
        self.add_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.GL_new_task.addWidget(self.add_btn, 0, 3, 1, 2)


        self.verticalLayout_2.addLayout(self.GL_new_task)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.d_label.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.p_label.setText(QCoreApplication.translate("MainWindow", u"priority", None))
        self.is_done_label.setText(QCoreApplication.translate("MainWindow", u"is done!", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.new_title.setText(QCoreApplication.translate("MainWindow", u"title", None))
        self.new_description.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas','monospace'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; font-style:italic; text-decoration: underline;\">description</span></p></body></html>", None))
        self.new_time.setText(QCoreApplication.translate("MainWindow", u"time:", None))
        self.new_date.setText(QCoreApplication.translate("MainWindow", u"date:", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

