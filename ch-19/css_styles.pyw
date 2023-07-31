from PyQt6 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(
    "QGroupBox QLabel {color: blue;} QPushButton {font-style: italic}"
)
window = QtWidgets.QWidget()
window.setWindowTitle("Таблицы стилей")
window.setStyleSheet("QLabel#first {color: green;} QLabel:hover {color: red;}")
window.resize(200, 150)
lbl1 = QtWidgets.QLabel("Зеленый текст")
lbl1.setObjectName("first")
lbl2 = QtWidgets.QLabel("Полужирный текст")
lbl2.setStyleSheet("font-weight: bold")
lbl3 = QtWidgets.QLabel("Синий текст")
btn = QtWidgets.QPushButton("Курсивный текст")
box = QtWidgets.QGroupBox("Группа")
bbox = QtWidgets.QVBoxLayout()
bbox.addWidget(lbl3)
box.setLayout(bbox)
mainbox = QtWidgets.QVBoxLayout()
mainbox.addWidget(lbl1)
mainbox.addWidget(lbl2)
mainbox.addWidget(box)
mainbox.addWidget(btn)
window.setLayout(mainbox)
window.show()
sys.exit(app.exec())
