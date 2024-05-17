# -*- coding: utf-8 -*-
import sys
# Form implementation generated from reading ui file 'D:\Python_code\Longfier_Potel_De-Beer\code\combat.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_combat_window(object):
    def setupUi(self, combat_window):
        self.spe2 = 'False'

        self.pokemon1 = ""
        self.pokemon2 = ""

        self.background_label = QtWidgets.QLabel(combat_window)
        self.background_label.setGeometry(QtCore.QRect(200, -200, 1100, 834))
        print(self.pokemon1)
        self.background_label.setPixmap(QtGui.QPixmap(self.pokemon1))

        self.ground_label = QtWidgets.QLabel(combat_window)
        self.ground_label.setGeometry(QtCore.QRect(200, -113, 1100, 834))
        self.ground_label.setPixmap(QtGui.QPixmap("ressources/SolCombat.png"))
        self.ground_label.setStyleSheet("background-color: transparent;")
        self.ground_label.raise_()

        self.pokemon1_label = QtWidgets.QLabel(combat_window)
        self.pokemon1_label.setGeometry(QtCore.QRect(200, -113, 1100, 834))
        self.pokemon1_label.setPixmap(QtGui.QPixmap(self.pokemon1))
        self.pokemon1_label.setStyleSheet("background-color: transparent;")
        self.pokemon1_label.raise_()

        self.pokemon2_label = QtWidgets.QLabel(combat_window)
        self.pokemon2_label.setGeometry(QtCore.QRect(200, -113, 1100, 834))
        self.pokemon2_label.setPixmap(QtGui.QPixmap(self.pokemon2))
        self.pokemon2_label.setStyleSheet("background-color: transparent;")
        self.pokemon2_label.raise_()



        combat_window.setObjectName("combat_window")
        combat_window.resize(1100, 834)
        self.attack_button = QtWidgets.QPushButton(combat_window)
        self.attack_button.setGeometry(QtCore.QRect(200, 510, 300, 120))
        self.attack_button.setObjectName("attack_button")
        self.run_button = QtWidgets.QPushButton(combat_window)
        self.run_button.setGeometry(QtCore.QRect(600, 650, 300, 120))
        self.run_button.setObjectName("run_button")
        self.bag_button = QtWidgets.QPushButton(combat_window)
        self.bag_button.setGeometry(QtCore.QRect(200, 650, 300, 120))
        self.bag_button.setObjectName("bag_button")
        self.pokemon_button = QtWidgets.QPushButton(combat_window)
        self.pokemon_button.setGeometry(QtCore.QRect(600, 510, 300, 120))
        self.pokemon_button.setObjectName("pokemon_button")

        self.att_normal_button = QtWidgets.QPushButton(combat_window)
        self.att_normal_button.setGeometry(QtCore.QRect(200, 510, 300, 120))
        self.att_normal_button.setObjectName("Attaque normal bouton")
        self.att_normal_button.hide()

        self.att_spe1_button = QtWidgets.QPushButton(combat_window)
        self.att_spe1_button.setGeometry(QtCore.QRect(600, 510, 300, 120))
        self.att_spe1_button.setObjectName("Attaque spéciale bouton")
        self.att_spe1_button.hide()

        self.att_spe2_button = QtWidgets.QPushButton(combat_window)
        self.att_spe2_button.setGeometry(QtCore.QRect(400, 370, 300, 120))
        self.att_spe2_button.setObjectName("Attaque spéciale bouton")
        self.att_spe2_button.hide()

        self.att_exit_button = QtWidgets.QPushButton(combat_window)
        self.att_exit_button.setGeometry(QtCore.QRect(400, 650, 300, 120))
        self.att_exit_button.setObjectName("Retour")
        self.att_exit_button.hide()

        self.poke_switch_1 = QtWidgets.QPushButton(combat_window)
        self.poke_switch_1.setGeometry(QtCore.QRect(200, 230, 300, 120))
        self.poke_switch_1.setObjectName("Pokemon 1")
        self.poke_switch_1.hide()

        self.poke_switch_2 = QtWidgets.QPushButton(combat_window)
        self.poke_switch_2.setGeometry(QtCore.QRect(600, 230, 300, 120))
        self.poke_switch_2.setObjectName("Pokemon 2")
        self.poke_switch_2.hide()

        self.poke_switch_3 = QtWidgets.QPushButton(combat_window)
        self.poke_switch_3.setGeometry(QtCore.QRect(200, 370, 300, 120))
        self.poke_switch_3.setObjectName("Pokemon 3")
        self.poke_switch_3.hide()

        self.poke_switch_4 = QtWidgets.QPushButton(combat_window)
        self.poke_switch_4.setGeometry(QtCore.QRect(600, 370, 300, 120))
        self.poke_switch_4.setObjectName("Pokemon 4")
        self.poke_switch_4.hide()

        self.poke_switch_5 = QtWidgets.QPushButton(combat_window)
        self.poke_switch_5.setGeometry(QtCore.QRect(200, 510, 300, 120))
        self.poke_switch_5.setObjectName("Pokemon 5")
        self.poke_switch_5.hide()

        self.poke_switch_6 = QtWidgets.QPushButton(combat_window)
        self.poke_switch_6.setGeometry(QtCore.QRect(600, 510, 300, 120))
        self.poke_switch_6.setObjectName("Pokemon 6")
        self.poke_switch_6.hide()

        self.poke_exit_button = QtWidgets.QPushButton(combat_window)
        self.poke_exit_button.setGeometry(QtCore.QRect(400, 650, 300, 120))
        self.poke_exit_button.setObjectName("Retour")
        self.poke_exit_button.hide()


        self.attack_button.pressed.connect(self.combat_pressed)
        self.att_exit_button.pressed.connect(self.retour_pressed)
        self.poke_exit_button.pressed.connect(self.retour_pressed)
        self.pokemon_button.pressed.connect(self.poke_pressed)


        self.retranslateUi(combat_window)
        QtCore.QMetaObject.connectSlotsByName(combat_window)

    def retranslateUi(self, combat_window):
        _translate = QtCore.QCoreApplication.translate
        combat_window.setWindowTitle(_translate("combat_window", "Combat"))
        self.attack_button.setText(_translate("combat_window", "ATTAQUE"))
        self.run_button.setText(_translate("combat_window", "FUITE"))
        self.bag_button.setText(_translate("combat_window", "SAC"))
        self.pokemon_button.setText(_translate("combat_window", "POKEMON"))
        self.att_normal_button.setText(_translate("combat_window","NORMALE"))
        self.att_spe1_button.setText(_translate("combat_window", "SPECIALE 1"))
        self.att_spe2_button.setText(_translate("combat_window", "SPECIALE 2"))
        self.att_exit_button.setText(_translate("combat_window", "Retour"))
        self.poke_switch_1.setText(_translate("combat_window", "Pokemon 1"))
        self.poke_switch_2.setText(_translate("combat_window", "Pokemon 2"))
        self.poke_switch_3.setText(_translate("combat_window", "Pokemon 3"))
        self.poke_switch_4.setText(_translate("combat_window", "Pokemon 4"))
        self.poke_switch_5.setText(_translate("combat_window", "Pokemon 5"))
        self.poke_switch_6.setText(_translate("combat_window", "Pokemon 6"))
        self.poke_exit_button.setText(_translate("combat_window","Retour"))


    def combat_pressed(self):
        self.retour_pressed()
        self.attack_button.hide()
        self.run_button.hide()
        self.bag_button.hide()
        self.pokemon_button.hide()

        self.att_normal_button.show()
        self.att_spe1_button.show()
        self.att_exit_button.show()
        if self.spe2 == 'True' :
            self.att_spe2_button.show()

    def poke_pressed(self):
        self.retour_pressed()
        self.attack_button.hide()
        self.run_button.hide()
        self.bag_button.hide()
        self.pokemon_button.hide()

        self.poke_switch_1.show()
        self.poke_switch_2.show()
        self.poke_switch_3.show()
        self.poke_switch_4.show()
        self.poke_switch_5.show()
        self.poke_switch_6.show()
        self.poke_exit_button.show()

    def retour_pressed(self):
        self.attack_button.show()
        self.run_button.show()
        self.bag_button.show()
        self.pokemon_button.show()

        self.att_normal_button.hide()
        self.att_spe1_button.hide()
        self.att_spe2_button.hide()
        self.att_exit_button.hide()
        self.poke_switch_1.hide()
        self.poke_switch_2.hide()
        self.poke_switch_3.hide()
        self.poke_switch_4.hide()
        self.poke_switch_5.hide()
        self.poke_switch_6.hide()
        self.poke_exit_button.hide()

    def poke_ko(self):
        self.poke_pressed()
        self.poke_exit_button.hide()

    def closeEvent(self,event) :
        print("fermée")
        event.ignore()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    combat_window = QtWidgets.QWidget()
    ui = Ui_combat_window()
    ui.setupUi(combat_window)
    combat_window.show()
    sys.exit(app.exec_())