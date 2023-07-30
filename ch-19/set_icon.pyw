from PyQt6 import QtGui, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Смена значка в заголовке окна")
window.resize(400, 100)
ico = QtGui.QIcon("icon.png")
window.setWindowIcon(ico)
app.setWindowIcon(ico)
window.show()
sys.exit(app.exec())
