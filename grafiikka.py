import sys
from alustus import Alustus
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Grafiikka(QWidget):
    def __init__(self):
        super().__init__()

    def kysySyöte(self):
        self.label_kuvio = QLabel("Minkä kuvion haluat piirtää?")
        self.rb1 = QRadioButton("Viivadiagrammi",self)
        self.rbgroup1 = QButtonGroup()
        self.rbgroup1.addButton(self.rb1)
        self.rb1.clicked.connect(self.kuvionValinta)

        self.label_grid = QLabel("Haluatko piirtää kuvaajaan gridin?")
        self.rb2 = QRadioButton("Kyllä",self)
        self.rb3 = QRadioButton("Ei",self)
        self.rbgroup2 = QButtonGroup()
        self.rbgroup2.addButton(self.rb2)
        self.rbgroup2.addButton(self.rb3)
        self.rb2.clicked.connect(self.gridValinta)
        self.rb3.clicked.connect(self.gridValinta)

        self.label_data = QLabel("Anna datan nimi ja sijainti tekstikenttään.")
        self.kentta = QLineEdit()
        self.kentta.textChanged[str].connect(self.datanValinta)

        layout = QVBoxLayout()
        layout.addWidget(self.label_kuvio)
        layout.addWidget(self.rb1)

        layout.addWidget(self.label_grid)
        layout.addWidget(self.rb2)
        layout.addWidget(self.rb3)

        layout.addWidget(self.label_data)
        layout.addWidget(self.kentta)

        self.setGeometry(200,200,300,300)
        self.setLayout(layout)

        self.pb1 = QPushButton("Valmis", self)
        layout.addWidget(self.pb1)
        #self.pb1.clicked.connect(self.close)
        self.pb1.clicked.connect(self.valmistelu)
        self.pb1.clicked.connect(self.lahetys)

        self.show()

    def kuvionValinta(self):
        valinta = self.sender().text()
        if valinta == "Viivadiagrammi":
            alustus.tunniste = valinta
        else:
            print("Ei vielä implementoitu")

    def gridValinta(self):
        valinta = self.sender().text()
        if valinta == "Kyllä":
            alustus.grid = valinta
        else:
            alustus.grid = valinta

    def datanValinta(self, text):
        alustus.dataNimi = text

    def valmistelu(self):
        tiedosto = alustus.avaaTiedosto(alustus.dataNimi)
        alustus.lueData(tiedosto)
        alustus.laskeKa(alustus.data)
        alustus.laskeKeskihajonta(alustus.data, alustus.keskiarvo)

    def lahetys(self):
        self.g = MainWindow()
        self.g.show()

class Graafi(QGraphicsItem):
    def __init__(self):
        super(Graafi, self).__init__()
        self.testi = None

    def boundingRect(self):
        return QRectF(0,0,300,300)

    def paint(self, painter, option, widget):
        data = alustus.data
        painter.setPen(Qt.black)
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        #painter.drawEllipse(10,80,10,10)
        #painter.drawEllipse(20,60,10,10)
        #painter.drawLine(10,80,20,60)

        print(data)
        for n in range(len(data)):
            if n + 1 < len(data):
                painter.drawEllipse(int(data[n][0])*10, int(data[n][1])*10, 6, 6)
                painter.drawLine(int(data[n][0])*10, int(data[n][1])*10, int(data[n + 1][0])*10, int(data[n + 1][1])*10)
            else:
                painter.drawEllipse(int(data[n][0])*10, int(data[n][1])*10, 6, 6)
                painter.drawLine(int(data[n - 1][0])*10, int(data[n - 1][1])*10, int(data[n][0])*10, int(data[n][1])*10)


class MainWindow(QGraphicsView):
    def __init__(self):
        super(MainWindow, self).__init__()
        scene = QGraphicsScene(self)
        self.graafi = Graafi()
        scene.addItem(self.graafi)
        scene.setSceneRect(0,0,300,300)
        self.setScene(scene)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    alustus = Alustus()
    gra = Grafiikka()
    gra.kysySyöte()
    sys.exit(app.exec_())









