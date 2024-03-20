import sys
import json
from PySide6 import QtWidgets, QtGui, QtCore
from qt_material import apply_stylesheet
import functions.card as card


with open('config.json', 'r') as file:
  config = json.load(file)

application = config.get('application')

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle(application['name'])
    self.setFixedSize(application['size']['width'], application['size']['height'])

    main_widget = QtWidgets.QWidget()
    self.setCentralWidget(main_widget)

    image = QtGui.QPixmap('images/default.png')
    scaled_image = image.scaled(252, 352, QtCore.Qt.AspectRatioMode.KeepAspectRatio)

    image_button = QtWidgets.QPushButton()
    image_button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    image_button.setStyleSheet('background-color: transparent;border: 1px solid #FFFFFF')
    image_button.setIcon(QtGui.QIcon(scaled_image))
    image_button.setIconSize(QtCore.QSize(252, 352))
    image_button.clicked.connect(lambda: card.load(image_button))

    text_label = QtWidgets.QLabel("這裡是文字顯示區域")
    text_label.setStyleSheet('border: 1px solid #FFFFFF')
    text_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

    layout = QtWidgets.QHBoxLayout(main_widget)
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(10)
    layout.addWidget(image_button, 4)
    layout.addWidget(text_label, 6)

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  app_icon = QtGui.QIcon('images/koikatu.ico')
  app.setWindowIcon(app_icon)

  apply_stylesheet(app, theme=application['theme'])

  window = MainWindow()
  window.show()

  sys.exit(app.exec())