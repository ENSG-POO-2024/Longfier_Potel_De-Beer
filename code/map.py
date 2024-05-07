import joueur
from tools import *
from combat_gab import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random as rd
import numpy as np



class Carte(QWidget):
    def __init__(self):
        super().__init__()

        self.coord = [rd.randint(1000,3000), rd.randint(1000,3000)]
        self.cam_size = 5
        self.taille_map = int(np.max(tableau_travail)) + 1


        #Création de la fenêtre principale
        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('Pokemon mais en plus gèze')

        #Changement de l'icone de l'app
        self.icone = QIcon('ressources/pokeball_icone.png')
        self.setWindowIcon(self.icone)

        #Initialisation du fond
        self.state = 'start_screen'
        self.background = QPixmap('ressources/Background.png').scaledToHeight(self.height())

        # Initialisation du layout
        self.temp = QHBoxLayout()
        self.label_temp = QLabel('oui')
        self.temp.addWidget(self.label_temp)


        self.layout_verti = QVBoxLayout(self)
        self.layout_verti.addLayout(self.temp)

        print(self.layout_verti.itemAt(0))
        self.startScreen()

    def paintEvent(self, event):
        if self.state == 'start_screen':

            painter = QPainter(self)
            painter.drawPixmap(-275, 0, self.background)

        else:

            self.paintMap()

    def startScreen(self):

        #Initialisation du bouton
        self.start_button = QPushButton(text='Start game', parent=self)
        self.start_button.setGeometry(350, 530, 200, 100)
        self.start_button.show()
        self.start_button.clicked.connect(self.start_game)
        self.start_button.setStyleSheet(
            "QPushButton {"
            "color: black;"
            "background-color: transparent;"
            "font-size: 24px;"
            "font-weight: bold"
            "}"
        )

    def start_game(self):
        equipe = [Pokemon('Bulbasaur'), Pokemon('Charmander'), Pokemon('Squirtle')]
        player = joueur.Joueur([self.coord], equipe)

        self.start_button.hide()
        self.global_map = creaMap()
        self.state = 'game_screen'


    def paintMap(self):

        x_min = self.coord[0] - self.cam_size//2
        x_max = self.coord[0] + self.cam_size//2
        y_min = self.coord[1] - self.cam_size//2
        y_max = self.coord[1] + self.cam_size//2

        if x_min < 0 :
            x_min = 0
            x_max = x_min + self.cam_size - 1
        elif x_max > self.taille_map:
            x_max = self.taille_map
            x_min = x_max + self.cam_size - 1
        if y_min < 0:
            y_min = 0
            y_max = y_min + self.cam_size - 1
        elif y_max > self.taille_map :
            y_max = self.taille_map
            y_min = y_max + self.cam_size - 1

        # Effacez le contenu précédent du layout_verti uniquement si nécessaire
        if self.layout_verti.count() > 0:
            for i in reversed(range(self.layout_verti.count())):
                layout_to_remove = self.layout_verti.itemAt(i)
                for j in reversed(range(layout_to_remove.count())):
                    widget = layout_to_remove.itemAt(j).widget()
                    layout_to_remove.removeWidget(widget)
                    widget.setParent(None)
                self.layout_verti.removeItem(layout_to_remove)

        for i in range(x_min, x_max):
            layout_horiz = QHBoxLayout()
            for j in range(y_min, y_max):
                pixmap = self.dessinPixmap(self.global_map[i,j])
                if pixmap:
                    label = QLabel()
                    label.setPixmap(pixmap)
                    layout_horiz.addWidget(label)
            self.layout_verti.addLayout(layout_horiz)

    def dessinPixmap(self,valeur):


        if valeur == '0.0' :
            print('pixmap')
            pixmap = QPixmap(64,64)
            pixmap.fill(QColor(166,247,64))
            texture = QPixmap( mapToSprite['0'])
            painter = QPainter(pixmap)
            painter.drawPixmap(0,0,texture)
            painter.end()

            return pixmap
        else :
            return None


if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = Carte()
    widget.show()
    sys.exit(app.exec_())


