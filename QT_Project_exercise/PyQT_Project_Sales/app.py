import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from LoginForms.MainMenuForm import MainMenuWindow

class MainWindow(MainMenuWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show()

		#add as any properties here...

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    main = MainWindow()

    sys.exit(app.exec())