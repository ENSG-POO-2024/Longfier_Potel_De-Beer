import joueur
from tools import *
from combat_gab import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QPixmap, QIcon

#Creation de la map
taille_map = int(np.max(tableau_travail)) + 1

# 0 : bloc de déplacement libre
# 1 : blocs solides
# nom de pokemon : hautes herbes où spawn le pokémon
map = np.zeros([taille_map, taille_map]).astype(str)

for i in range(len(tableau_travail)):
    map[tableau_travail[i, 0], tableau_travail[i, 1]] = data_array[i + 1, 0]

print(map)


class Carte(QWidget):
    def __init__(self):
        super().__init__()

        #Création de la fenêtre principale
        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('Pokemon mais en plus gèze')

        #Changement de l'icone de l'app
        self.icone = QIcon('ressources/pokeball_icone.png')
        self.setWindowIcon(self.icone)

        #Initialisation du fond
        self.state = 'start_screen'
        self.background = QPixmap('ressources/Background.png').scaledToHeight(self.height())

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
        try:
            #equipe = [Pokemon('Bulbasaur'), Pokemon('Charmander'), Pokemon('Squirtle')]
            #player = joueur.Joueur([taille_map / 2, taille_map / 2], equipe)
            self.start_button.hide()




    def paintMap(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Carte()
    widget.show()
    sys.exit(app.exec_())
