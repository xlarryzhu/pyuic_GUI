# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Dev/1Projects/PyQtTool/pyuic_GUI/MainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(600, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Main)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton_out = QtWidgets.QToolButton(Main)
        self.toolButton_out.setMinimumSize(QtCore.QSize(0, 20))
        self.toolButton_out.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_out.setCheckable(False)
        self.toolButton_out.setObjectName("toolButton_out")
        self.gridLayout.addWidget(self.toolButton_out, 1, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(20, 20))
        self.label_4.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_op = QtWidgets.QLineEdit(Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_op.sizePolicy().hasHeightForWidth())
        self.lineEdit_op.setSizePolicy(sizePolicy)
        self.lineEdit_op.setMinimumSize(QtCore.QSize(200, 20))
        self.lineEdit_op.setObjectName("lineEdit_op")
        self.gridLayout.addWidget(self.lineEdit_op, 3, 1, 1, 4)
        self.lineEdit_out = QtWidgets.QLineEdit(Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_out.sizePolicy().hasHeightForWidth())
        self.lineEdit_out.setSizePolicy(sizePolicy)
        self.lineEdit_out.setMinimumSize(QtCore.QSize(260, 20))
        self.lineEdit_out.setObjectName("lineEdit_out")
        self.gridLayout.addWidget(self.lineEdit_out, 1, 1, 1, 4)
        self.toolButton_in = QtWidgets.QToolButton(Main)
        self.toolButton_in.setMaximumSize(QtCore.QSize(16777215, 20))
        self.toolButton_in.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_in.setObjectName("toolButton_in")
        self.gridLayout.addWidget(self.toolButton_in, 0, 6, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(Main)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 4, 3, 1, 1)
        self.lineEdit_in = QtWidgets.QLineEdit(Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_in.sizePolicy().hasHeightForWidth())
        self.lineEdit_in.setSizePolicy(sizePolicy)
        self.lineEdit_in.setMinimumSize(QtCore.QSize(260, 20))
        self.lineEdit_in.setObjectName("lineEdit_in")
        self.gridLayout.addWidget(self.lineEdit_in, 0, 1, 1, 4)
        self.checkBox_exec = QtWidgets.QCheckBox(Main)
        self.checkBox_exec.setObjectName("checkBox_exec")
        self.gridLayout.addWidget(self.checkBox_exec, 4, 2, 1, 1)
        self.checkBox_preview = QtWidgets.QCheckBox(Main)
        self.checkBox_preview.setObjectName("checkBox_preview")
        self.gridLayout.addWidget(self.checkBox_preview, 4, 4, 1, 1)
        self.checkBox_debug = QtWidgets.QCheckBox(Main)
        self.checkBox_debug.setObjectName("checkBox_debug")
        self.gridLayout.addWidget(self.checkBox_debug, 4, 1, 1, 1)
        self.pushButton_OK = QtWidgets.QPushButton(Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_OK.sizePolicy().hasHeightForWidth())
        self.pushButton_OK.setSizePolicy(sizePolicy)
        self.pushButton_OK.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_OK.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_OK.setFont(font)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout.addWidget(self.pushButton_OK, 3, 6, 2, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(Main)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.textBrowser = QtWidgets.QTextBrowser(Main)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)
        Main.setTabOrder(self.toolButton_in, self.toolButton_out)
        Main.setTabOrder(self.toolButton_out, self.lineEdit_in)
        Main.setTabOrder(self.lineEdit_in, self.textBrowser)
        Main.setTabOrder(self.textBrowser, self.lineEdit_op)
        Main.setTabOrder(self.lineEdit_op, self.lineEdit_out)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "PyQt Tools(.ui to .py) "))
        self.toolButton_out.setText(_translate("Main", "..."))
        self.label_3.setText(_translate("Main", "Output File(.py) Path:"))
        self.label_2.setText(_translate("Main", "Input File(.ui) Path:"))
        self.label_4.setText(_translate("Main", "Additional Options:"))
        self.toolButton_in.setText(_translate("Main", "..."))
        self.checkBox_5.setText(_translate("Main", "from-imports"))
        self.checkBox_exec.setText(_translate("Main", "Exective"))
        self.checkBox_preview.setText(_translate("Main", "Preview"))
        self.checkBox_debug.setText(_translate("Main", "Debug"))
        self.pushButton_OK.setText(_translate("Main", "OK"))

