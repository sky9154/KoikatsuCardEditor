from PySide6 import QtWidgets


class EditFrame(QtWidgets.QFrame):
  def __init__(self):
    super().__init__()

    self.setContentsMargins(10, 10, 10, 10)
    self.setStyleSheet('background-color: transparent; border: 1px solid #FFFFFF;')