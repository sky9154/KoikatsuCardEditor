from PySide6 import QtWidgets, QtGui, QtCore
from kkloader import KoikatuCharaData
import json


def load(image_button):
  file_dialog = QtWidgets.QFileDialog()
  file_dialog.setWindowTitle('選擇卡片')
  file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
  file_dialog.setDirectory(QtCore.QDir.homePath() + '/Downloads')
  file_dialog.setNameFilter('*.png')

  if file_dialog.exec():
    files = file_dialog.selectedFiles()
    card_path = files[0] if files else None

    if card_path:
      pixmap = QtGui.QPixmap(card_path)
      scaled_pixmap = pixmap.scaled(252, 352, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
      image_button.setIcon(QtGui.QIcon(scaled_pixmap))

    return card_path

def info(card_path):
  try:
    kc = KoikatuCharaData.load(card_path)
    character = kc['Parameter']

    with open('assets/data/blood.json', 'r') as blood_json:
      blood = json.load(blood_json)

    with open('assets/data/personality.json', 'r') as personality_json:
      personality = json.load(personality_json)

    return {
      'lastname': character['lastname'],
      'firstname': character['firstname'],
      'nickname': character['nickname'],
      'sex': 'male' if character['sex'] == 0 else 'female',
      'personality': personality[str(character['personality'])],
      'bloodType': blood[str(character['bloodType'])],
      'birthMonth': character['birthMonth'],
      'birthDay': character['birthDay']
    }
  except Exception as e:
    return {
      'lastname': '', 'firstname': '', 'nickname': '', 'sex': '',
      'personality': '', 'bloodType': '', 'birthMonth': '', 'birthDay': ''
    }