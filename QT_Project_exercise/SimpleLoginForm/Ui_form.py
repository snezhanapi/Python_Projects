# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/nemsys/data/projects/courses/netIT/PythonCourseNetIT/PythonCourse_25.10-Labs/PyQT/SimpleLoginForm/form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(556, 501)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 30, 284, 57))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 130, 451, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.leUserName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.leUserName.setObjectName("leUserName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leUserName)
        self.lePass = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lePass.setObjectName("lePass")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lePass)
        self.btnSubmit = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnSubmit.setObjectName("btnSubmit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btnSubmit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Simple Login Form"))
        self.label_2.setText(_translate("Form", "user name"))
        self.label_3.setText(_translate("Form", "password"))
        self.btnSubmit.setText(_translate("Form", "Submit"))