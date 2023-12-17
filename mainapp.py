from PyQt5.QtWidgets import QApplication, QWidget

main_app = QApplication([])

window = QWidget(windowTitle="HelloWorld")
window.show()

main_app.exec()
