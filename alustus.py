class Alustus():

    def __init__(self):
        self.tunniste = None
        self.grid = None
        self.dataNimi = None
        self.data = []
        self.keskiarvo = None
        self.keskihajonta = None

    """Avaa ja palauttaa halutun tiedoston. Saa parametrina tiedoston sijainnin/nimen."""
    def avaaTiedosto(self, nimi):
        try:
            file = open(nimi)
            return file
        except:
            print("Tiedoston nimellä ei löytynyt tiedostoa.")


    def lueData(self, data):
        for line in data:
            line = line.strip().split(" ")
            try:
                lisays = (float(line[0]), float(line[1]))
                self.data.append(lisays)
            except:
                pass

    def laskeKa(self, data):
        sum = 0
        for line in data:
            sum += line[1]
        ka = sum / len(data)
        self.keskiarvo = ka

    def laskeKeskihajonta(self, data, keskiarvo):
        sum = 0
        for line in data:
            sum += (line[1] - keskiarvo)**2
        hajonta = (sum / (len(data)-1))**(1/2)
        self.keskihajonta = hajonta

