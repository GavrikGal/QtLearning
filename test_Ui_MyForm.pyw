from PyQt6 import QtWidgets
import ui_MyForm


class MyWindow(QtWidgets.QWidget):
    def __inti__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = ui_MyForm.Ui_myForm()
        self.ui.setupUi(self)
        self.ui.btnQuit.clicked.connect(QtWidgets.QApplication.instance().quit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
