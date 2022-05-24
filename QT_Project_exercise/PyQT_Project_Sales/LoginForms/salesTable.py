from email import header
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from db import DB

class Table(qtw.QTableWidget):
	def __init__(self, parent):
		super().__init__()
		self.data = self.load_data()
		self.createTable(parent)



	def createTable(self,parent):
		rows = len(self.data['data'])
		cols = len(self.data['header'])

		# init table
		table = qtw.QTableWidget(parent=parent)
		table.setRowCount(rows)
		table.setColumnCount(cols)
		table.setHorizontalHeaderLabels(self.data['header'])
		# table.setMinimumHeight(rows*100)
		# table.setMinimumWidth(cols*300)

		# set data
		for i,row in enumerate(self.data['data']):
			for j,item in enumerate(row):
				table.setItem(i,j,qtw.QTableWidgetItem(item))

		table.resizeColumnsToContents()

		# streach table:
		# table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
		# table.verticalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)



		self.table = table
		# self.table.show()

	def load_data(self):
		header = ("a","b","c","d","e","f","g")
		data = list(['Sale1', 's'])
		self.db = DB()
		#data = self.db.view_sales()
		#(1, datetime.date(2022, 1, 28), 1, 'Sale1', 1, 1, 10000.0)

		print(data)

		return {
			"header":header,
			"data":data
		}

class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.table = Table(parent=self)

		self.show();


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())