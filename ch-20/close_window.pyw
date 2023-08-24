from PyQt6 import QtWidgets, QtGui


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(500, 300)

    def closeEvent(self, e: QtGui.QCloseEvent) -> None:
        result = QtWidgets.QMessageBox.question(self,
                                                "Подтверждение закрытия окна",
                                                "Вы действительно хотите закрыть окно?")
        if result ==QtWidgets.QMessageBox.StandardButton.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
        else:
            e.ignore()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
