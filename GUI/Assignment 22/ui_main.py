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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(427, 547)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.GL_tasks = QGridLayout()
        self.GL_tasks.setObjectName(u"GL_tasks")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.GL_tasks.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)

        self.GL_tasks.addWidget(self.checkBox_3, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.GL_tasks.addWidget(self.pushButton, 1, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.GL_tasks.addWidget(self.pushButton_3, 3, 3, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.GL_tasks.addWidget(self.pushButton_6, 3, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.GL_tasks.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)

        self.GL_tasks.addWidget(self.checkBox_2, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.GL_tasks.addWidget(self.pushButton_2, 2, 3, 1, 1)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.GL_tasks.addWidget(self.checkBox, 1, 0, 1, 1)

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

        self.p_label = QLabel(self.centralwidget)
        self.p_label.setObjectName(u"p_label")
        sizePolicy1.setHeightForWidth(self.p_label.sizePolicy().hasHeightForWidth())
        self.p_label.setSizePolicy(sizePolicy1)
        self.p_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.GL_tasks.addWidget(self.p_label, 0, 2, 1, 1)

        self.d_label = QLabel(self.centralwidget)
        self.d_label.setObjectName(u"d_label")
        sizePolicy.setHeightForWidth(self.d_label.sizePolicy().hasHeightForWidth())
        self.d_label.setSizePolicy(sizePolicy)
        self.d_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.GL_tasks.addWidget(self.d_label, 0, 3, 1, 1)

        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.GL_tasks.addWidget(self.checkBox_4, 1, 2, 1, 1)

        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)
        self.checkBox_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.GL_tasks.addWidget(self.checkBox_5, 2, 2, 1, 1)

        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy)
        self.checkBox_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.GL_tasks.addWidget(self.checkBox_6, 3, 2, 1, 1)


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
        font.setPointSize(20)
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
        font1.setPointSize(20)
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
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.checkBox_3.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.checkBox_2.setText("")
        self.pushButton_2.setText("")
        self.checkBox.setText("")
        self.is_done_label.setText(QCoreApplication.translate("MainWindow", u"is done!", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.p_label.setText(QCoreApplication.translate("MainWindow", u"priority", None))
        self.d_label.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.checkBox_4.setText("")
        self.checkBox_5.setText("")
        self.checkBox_6.setText("")
        self.new_title.setText(QCoreApplication.translate("MainWindow", u"title", None))
        self.new_description.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; text-decoration: underline;\">description</span></p></body></html>", None))
        self.new_time.setText(QCoreApplication.translate("MainWindow", u"time:", None))
        self.new_date.setText(QCoreApplication.translate("MainWindow", u"date:", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

