import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from LoginForms.db import DB
from LoginForms.MainMenuForm import MainMenuWindow


class MainWindow(MainMenuWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.db = DB()
		self.db.view_sales()




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())