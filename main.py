from PySide6 import QtWidgets, QtGui
from qt_material import apply_stylesheet
import sys
import json
import components.Button as Button
import components.Frame as Frame
import components.Layout as Layout
import functions.card as Card


with open('assets/data/config.json', 'r') as config_json:
  config = json.load(config_json)

application = config.get('application')

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle(application['name'])
    self.setFixedSize(application['size']['width'], application['size']['height'])

    character = Card.info(None)

    main_widget = QtWidgets.QWidget()
    self.setCentralWidget(main_widget)

    self.image_button = Button.LoadButton()
    self.edit_frame = Frame.EditFrame()
    self.edit_layout = Layout.EditLayout(self.edit_frame, character)

    self.image_button.clicked.connect(self.load_image)

    self.main_layout = QtWidgets.QHBoxLayout(main_widget)
    self.main_layout.setContentsMargins(10, 10, 10, 10)
    self.main_layout.setSpacing(10)
    self.main_layout.addWidget(self.image_button, 4)
    self.main_layout.addWidget(self.edit_frame, 6)

  def load_image(self):
    card_path = Card.load(self.image_button)
    character = Card.info(card_path)

    self.main_layout.removeWidget(self.edit_frame)
    for child in self.edit_frame.findChildren(QtWidgets.QLineEdit):
      child.clear()

    self.edit_frame = Frame.EditFrame()
    self.edit_layout = Layout.EditLayout(self.edit_frame, character)
    self.main_layout.addWidget(self.edit_frame, 6)

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  app_icon = QtGui.QIcon('assets/images/koikatu.ico')
  app.setWindowIcon(app_icon)

  apply_stylesheet(app, theme=application['theme'])

  window = MainWindow()
  window.show()

  sys.exit(app.exec())