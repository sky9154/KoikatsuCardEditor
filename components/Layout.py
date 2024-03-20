from PySide6 import QtWidgets


class EditLayout(QtWidgets.QVBoxLayout):
  def __init__(self, edit_frame, character):
    super().__init__()

    edit_layout = QtWidgets.QVBoxLayout(edit_frame)
    edit_layout.setContentsMargins(10, 10, 10, 10)
    edit_layout.setSpacing(10)

    for key, value in character.items():
      label = QtWidgets.QLabel(key.upper())
      label.setStyleSheet('border: transparent;')
      line_edit = QtWidgets.QLineEdit(str(value))
      line_edit.setStyleSheet('color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 0px;')
      layout = QtWidgets.QHBoxLayout()
      layout.addWidget(label, 3)
      layout.addWidget(line_edit, 7)
      edit_layout.addLayout(layout)