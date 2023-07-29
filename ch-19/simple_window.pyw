from PyQt6 import QtWidgets, QtCore
import sys, time


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Заголовок окна")
window.resize(300, 50)
window.move(window.width() * -2, 0)
window.show()

x = (window.screen().availableSize().width() - window.frameSize().width()) // 2
y = (window.screen().availableSize().height() - window.frameSize().height()) // 2
window.move(x, y)

for i in range(1, 11):
    frame_geometry = window.frameGeometry()
    frame_geometry.setWidth(frame_geometry.width() + 10)
    print(frame_geometry)
    time.sleep(0.3)
    window.setGeometry((window.screen().availableSize().width() - frame_geometry.width()) // 2,
                       (window.screen().availableSize().height() - frame_geometry.height()) // 2,
                       frame_geometry.width(),
                       frame_geometry.height())
    window.hide()
    window.show()
sys.exit(app.exec())
