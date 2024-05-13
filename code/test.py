import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import combat_window

class Ui_echap_window(object):
    def setupUi(self, echap_window):
        echap_window.setObjectName("echap_window")
        echap_window.resize(1000, 650)
        self.resume_button = QtWidgets.QPushButton(echap_window)
        self.resume_button.setGeometry(QtCore.QRect(300, 80, 400, 90))
        self.resume_button.setObjectName("resume_button")
        self.quit_button = QtWidgets.QPushButton(echap_window)
        self.quit_button.setGeometry(QtCore.QRect(300, 480, 400, 90))
        self.quit_button.setObjectName("quit_button")
        self.settings_button = QtWidgets.QPushButton(echap_window)
        self.settings_button.setGeometry(QtCore.QRect(300, 280, 400, 90))
        self.settings_button.setObjectName("settings_button")

        self.retranslateUi(echap_window)
        QtCore.QMetaObject.connectSlotsByName(echap_window)

    def retranslateUi(self, ehcap_window):
        _translate = QtCore.QCoreApplication.translate
        ehcap_window.setWindowTitle(_translate("echap_window", "Echap"))
        self.resume_button.setText(_translate("echap_window", "Continuer"))
        self.quit_button.setText(_translate("echap_window", "Quitter"))
        self.settings_button.setText(_translate("echap_window", "Paramètres"))

class EchapWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_echap_window()
        self.ui.setupUi(self)
        self.setWindowTitle("Echap")
        self.ui.resume_button.clicked.connect(self.afficher_ui_combat)
        self.ui_combat_window_affichee = False  # Variable pour suivre l'état de la fenêtre Ui_echap_window

    def afficher_ui_combat(self):
        if not self.ui_combat_window_affichee:  # Si la fenêtre Ui_combat_window n'est pas affichée
            self.ui_combat_window = QtWidgets.QMainWindow()
            self.ui_combat = combat_window.Ui_combat_window()  # Instanciation de la classe Ui_combat_window
            self.ui_combat.setupUi(self.ui_combat_window)  # Configuration de l'interface
            self.ui_combat_window.show()  # Affichage de la fenêtre de combat
            self.ui_combat_window_affichee = True  # Mettre à jour l'état
        else:  # Si la fenêtre Ui_combat_window est déjà affichée
            self.ui_combat_window.hide()  # Masquer la fenêtre de combat
            self.ui_combat_window_affichee = False  # Mettre à jour l'état

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EchapWindow()
    window.show()
    sys.exit(app.exec_())
