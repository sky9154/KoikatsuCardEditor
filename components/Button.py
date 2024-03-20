from PySide6 import QtWidgets, QtGui, QtCore


class LoadButton(QtWidgets.QPushButton):
  def __init__(self):
    super().__init__()

    image = QtGui.QPixmap('assets/images/default.png')
    scaled_image = image.scaled(252, 352, QtCore.Qt.AspectRatioMode.KeepAspectRatio)

    self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    self.setStyleSheet('background-color: transparent; border: 1px solid #FFFFFF;')
    self.setIcon(QtGui.QIcon(scaled_image))
    self.setIconSize(QtCore.QSize(252, 352))