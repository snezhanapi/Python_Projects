import sys
from PyQt6 import QtWidgets as qtw
from LoginForms import loginForm
from LoginForms import MainMenuForm

class MainWindow(qtw.QWidget, MainMenuForm):
	def __init__(self, *args, **kwargs):
	    super().__init__(self, *args, **kwargs)
        self.setupUi(self)

		#add as any properties here...


if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)

  main = MainWindow()
  main.show()

  sys.exit(app.exec())