# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vending_machine_gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(527, 459)
        Form.setMinimumSize(QSize(527, 430))
        Form.setMaximumSize(QSize(527, 459))
        Form.setStyleSheet(u"QWidget#Form{\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.488069 rgba(28, 29, 73, 255));\n"
"}\n"
"\n"
"\n"
"QFrame{\n"
"	background:transparent;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_9 = QFrame(Form)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setEnabled(True)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_status = QLabel(self.frame_11)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(400, 61))
        self.label_status.setMaximumSize(QSize(400, 61))
        font = QFont()
        font.setFamily(u"Terminal")
        font.setBold(False)
        font.setWeight(50)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"border-style: outset;\n"
"border-radius: 6px;\n"
"border-width: 2px;\n"
"border-color: rgb(60, 231, 195);\n"
"background-color: rgb(32, 33, 84);")
        self.label_status.setFrameShape(QFrame.NoFrame)
        self.label_status.setFrameShadow(QFrame.Plain)
        self.label_status.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_status, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.spacer = QSpacerItem(10, 28, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_8.addItem(self.spacer)

        self.progressbar = QProgressBar(self.frame_12)
        self.progressbar.setObjectName(u"progressbar")
        self.progressbar.setMinimumSize(QSize(65, 0))
        self.progressbar.setMaximumSize(QSize(65, 0))
        self.progressbar.setStyleSheet(u"#progressbar {\n"
"    border: 2px solid rgb(49, 191, 160);\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0;\n"
"}\n"
"#progressbar::chunk {\n"
"    background-color: rgb(49, 191, 160);\n"
"    width: 10px; \n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.progressbar.setValue(100)
        self.progressbar.setTextVisible(False)

        self.horizontalLayout_8.addWidget(self.progressbar)


        self.verticalLayout_5.addWidget(self.frame_12, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(481, 261))
        self.frame_7.setMaximumSize(QSize(481, 261))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 20)
        self.frame_products = QFrame(self.frame_7)
        self.frame_products.setObjectName(u"frame_products")
        self.frame_products.setEnabled(True)
        self.frame_products.setStyleSheet(u"QFrame#frame_products{border-style: outset;\n"
"	border-radius: 6px;\n"
"	border-width: 2px;\n"
"	border-color: rgb(60, 231, 195);\n"
"	background-color: rgba(28, 29, 73, 40);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgba(51, 53, 132, 40);\n"
"	border :2px solid;\n"
"	border-radius: 4px;\n"
"	border-color: rgb(60, 231, 195);\n"
"	color:  rgb(60, 231, 195) \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(18, 19, 48, 40);\n"
"	border-color:rgb(54, 207, 174)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: rgb(105, 95, 148);\n"
"	border-color: rgb(105, 95, 148);\n"
"}\n"
"\n"
"")
        self.frame_products.setFrameShape(QFrame.StyledPanel)
        self.frame_products.setFrameShadow(QFrame.Raised)
        self.frame_products.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.frame_products)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame_products)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(51, 41))
        self.label_2.setMaximumSize(QSize(51, 41))
        self.label_2.setPixmap(QPixmap(u"images/coffe.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pushButton_coffee = QPushButton(self.frame_4)
        self.pushButton_coffee.setObjectName(u"pushButton_coffee")
        self.pushButton_coffee.setEnabled(True)
        self.pushButton_coffee.setMinimumSize(QSize(148, 28))
        self.pushButton_coffee.setMaximumSize(QSize(148, 28))

        self.horizontalLayout_2.addWidget(self.pushButton_coffee)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_products)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(51, 41))
        self.label_3.setMaximumSize(QSize(51, 41))
        self.label_3.setPixmap(QPixmap(u"images/choco.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.pushButton_choco = QPushButton(self.frame_5)
        self.pushButton_choco.setObjectName(u"pushButton_choco")
        self.pushButton_choco.setMinimumSize(QSize(148, 28))
        self.pushButton_choco.setMaximumSize(QSize(148, 28))

        self.horizontalLayout_3.addWidget(self.pushButton_choco)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_products)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(51, 41))
        self.label_4.setMaximumSize(QSize(51, 41))
        self.label_4.setPixmap(QPixmap(u"images/water.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.pushButton_water = QPushButton(self.frame_6)
        self.pushButton_water.setObjectName(u"pushButton_water")
        self.pushButton_water.setMinimumSize(QSize(148, 28))
        self.pushButton_water.setMaximumSize(QSize(148, 28))

        self.horizontalLayout_4.addWidget(self.pushButton_water)


        self.verticalLayout.addWidget(self.frame_6)


        self.horizontalLayout_5.addWidget(self.frame_products)

        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 70, -1, 70)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 22))
        self.comboBox.setMaximumSize(QSize(74, 22))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    border-radius: 3px;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: rgb(255, 255, 255)\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton_add_coin = QPushButton(self.frame_2)
        self.pushButton_add_coin.setObjectName(u"pushButton_add_coin")
        self.pushButton_add_coin.setEnabled(True)
        self.pushButton_add_coin.setMinimumSize(QSize(74, 28))
        self.pushButton_add_coin.setMaximumSize(QSize(74, 28))
        font1 = QFont()
        font1.setFamily(u"Small Fonts")
        font1.setPointSize(6)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_add_coin.setFont(font1)
        self.pushButton_add_coin.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(51, 53, 132, 40);\n"
"	border :2px solid;\n"
"	border-radius: 4px;\n"
"	border-color: rgb(60, 231, 195);\n"
"	color:  rgb(60, 231, 195) \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: rgb(105, 95, 148);\n"
"	border-color: rgb(105, 95, 148);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(18, 19, 48, 40);\n"
"	border-color:rgb(54, 207, 174)\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_add_coin)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignVCenter)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_cancel = QPushButton(self.frame_8)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setMinimumSize(QSize(60, 28))
        self.pushButton_cancel.setMaximumSize(QSize(60, 28))
        font2 = QFont()
        font2.setFamily(u"Small Fonts")
        font2.setPointSize(7)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_cancel.setFont(font2)
        self.pushButton_cancel.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(51, 53, 132, 40);\n"
"	border :2px solid;\n"
"	border-radius: 4px;\n"
"	border-color: rgb(60, 231, 195);\n"
"	color:  rgb(60, 231, 195) \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(18, 19, 48, 40);\n"
"	border-color:rgb(54, 207, 174)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: rgb(105, 95, 148);\n"
"	border-color: rgb(105, 95, 148);\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_cancel)


        self.verticalLayout_2.addWidget(self.frame_8, 0, Qt.AlignVCenter)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame_9)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_status.setText(QCoreApplication.translate("Form", u"Hello! Insert coins and choose product. \n"
" Money: 0 EUR ", None))
        self.label_2.setText("")
        self.pushButton_coffee.setText(QCoreApplication.translate("Form", u"COFFEE - 1.50", None))
        self.label_3.setText("")
        self.pushButton_choco.setText(QCoreApplication.translate("Form", u"HOT CHOCOLATE - 1.00", None))
        self.label_4.setText("")
        self.pushButton_water.setText(QCoreApplication.translate("Form", u"HOT WATER - 0.50", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"1 EUR", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"0.5 EUR", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"0.2 EUR", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"0.1 EUR", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"0.05 EUR", None))

        self.pushButton_add_coin.setText(QCoreApplication.translate("Form", u"ADD COIN", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Form", u"CANCEL", None))
    # retranslateUi

