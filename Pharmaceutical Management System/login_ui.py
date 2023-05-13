# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1248, 805)
        Dialog.setAutoFillBackground(False)
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(330, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.u_name_label.setFont(font)
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(340, 410, 111, 61))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(480, 480, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")
        self.signu_btn = QtWidgets.QPushButton(Dialog)
        self.signu_btn.setGeometry(QtCore.QRect(670, 480, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signu_btn.setFont(font)
        self.signu_btn.setObjectName("signu_btn")
        self.username_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.username_lineEdit.setGeometry(QtCore.QRect(480, 310, 371, 61))
        self.username_lineEdit.setStyleSheet("QLineEdit{\n"
"    border:2px solid;\n"
"    border-radius: 20px;\n"
"    color: rgb(108, 112, 125);\n"
"}")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(480, 400, 371, 61))
        self.password_lineEdit.setStyleSheet("QLineEdit{\n"
"    border:2px solid;\n"
"    border-radius: 20px;\n"
"    color: rgb(108, 112, 125);\n"
"}")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(420, 110, 431, 151))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1251, 811))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.u_name_label.raise_()
        self.pass_label.raise_()
        self.login_btn.raise_()
        self.signu_btn.raise_()
        self.username_lineEdit.raise_()
        self.password_lineEdit.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.u_name_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Username</span></p></body></html>"))
        self.pass_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Password</span></p></body></html>"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.signu_btn.setText(_translate("Dialog", "Signup"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Login </span></p></body></html>"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
