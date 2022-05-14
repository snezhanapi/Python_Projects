import sys
from PyQt6 import QtWidgets as qtw

from LoginForms.MainMenuForm import MainMenuWindow

class MainWindow(qtw.QMainWindow, MainMenuWindow):
	def __init__(self, *args, **kwargs):
	    super(MainWindow, self).__init__(self, *args, **kwargs)
        self.show()

		#add as any properties here...

if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)

  main = MainWindow()


  sys.exit(app.exec())