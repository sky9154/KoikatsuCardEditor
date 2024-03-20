from PySide6 import QtWidgets, QtGui, QtCore
from kkloader import KoikatuCharaData


def load(image_button):
  file_dialog = QtWidgets.QFileDialog()
  file_dialog.setWindowTitle('選擇卡片')
  file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
  file_dialog.setNameFilter('*.png')

  if file_dialog.exec():
    files = file_dialog.selectedFiles()
    file_path = files[0] if files else None

    if file_path:
      pixmap = QtGui.QPixmap(file_path)
      scaled_pixmap = pixmap.scaled(252, 352, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
      image_button.setIcon(QtGui.QIcon(scaled_pixmap))

      info(file_path)

def info(card):
  kc = KoikatuCharaData.load(card)

  character = kc['Parameter']

  info = {
    'version': character['version'],
    'sex': 'male' if character['sex'] == 0 else 'female',
    'lastname': character['lastname'],
    'firstname': character['firstname'],
    'nickname': character['nickname'],
    'personality': character['personality'],
    'bloodType': character['bloodType'],
    'birthMonth': character['birthMonth'],
    'birthDay': character['birthDay']
  }

  return info