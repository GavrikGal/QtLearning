from PyQt6 import QtWidgets, QtCore
import sys, time


def on_clicked():
    button.setDisabled(True)
    for i in range(1, 21):
        QtWidgets.QApplication.instance().processEvents(
            QtCore.QEventLoop.ProcessEventsFlag.AllEvents, 1000
        )
        time.sleep(1)
        print("step -", i)
    button.setDisabled(False)


app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Запустить процесс")
button.resize(200, 40)
button.clicked.connect(on_clicked)
button.show()
sys.exit(app.exec())
