import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from LoginForms.db import DB
from PyQt6 import QtCore as qtc


class LoginForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Login Form')
		self.resize(500, 120)

		layout = QGridLayout()

		label_name = QLabel('<font size="4"> Email </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Please enter your email')
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(self.lineEdit_username, 0, 1)

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText('Please enter your password')
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)

		button_login = QPushButton('Login')
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)

		button_close = QPushButton('Close')
		button_close.clicked.connect(self.exit_application)
		layout.addWidget(button_close, 3, 0, 1, 1)
		layout.setRowMinimumHeight(2, 75)

		self.setLayout(layout)
		self.db = DB()


	@qtc.pyqtSlot(bool)
	def check_password(self):
		msg = QMessageBox()

		if self.db.authenticate(user_name=self.lineEdit_username.text(), password=self.lineEdit_password.text()):
			msg.setText('You are now logged in!')
			msg.setWindowTitle("Success")

			#msg.setIcon(qtw.QMessageBox.Information)
			msg.exec()
			app.quit()
		else:
			msg.setText('Incorrect Password!')
			msg.setWindowTitle("Warning")
			#msg.setIcon(qtw.QMessageBox.Information)
			#msg.setInformativeText("Some informative text")
			msg.exec()


	def exit_application(self):
		msg_exit = QMessageBox()
		msg_exit.setText('Do you want to close Sales Manager? ')
		msg_exit.exec()
		app.quit()


if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = LoginForm()
	form.show()

	sys.exit(app.exec())