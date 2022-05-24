import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from LoginForms.loginForm import LoginForm

class MainMenuWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Sales Management')
		self.setGeometry(200,200,600,400)

		self.show()
		self.add_menubar()
		self.add_statusbar("You are not logged in!")
		self.add_toolbar()
		self.open_login_form()



	def add_statusbar(self,text):
		s = qtw.QStatusBar(self)
		self.setStatusBar(s)
		s.showMessage(text)

	def add_menubar(self):
		# get the menu bar
		menubar = self.menuBar()

		# add menu items
		sales_menu = menubar.addMenu('&Sales')
		import_export_menu = menubar.addMenu('Import/Export')
		help_menu = menubar.addMenu('He&lp')

		# add actions
		view_action = sales_menu.addAction('View')
		enter_action = sales_menu.addAction('Enter sales')
		search_action = sales_menu.addAction('Search sales')
		import_action = import_export_menu.addAction("Import CSV")
		export_action = import_export_menu.addAction("Export CSV")
		# add separator
		sales_menu.addSeparator()
	def add_toolbar(self):
		toolbar = self.addToolBar('File')
	def open_login_form(self):
		self.form = LoginForm()
		self.form.show()



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)

	window = MainMenuWindow()

	sys.exit(app.exec())