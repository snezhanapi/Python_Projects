import sys

from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt6 App Works')
#comment

window.setGeometry(100, 100, 500, 500)

window.show()
sys.exit(app.exec())