class Perros(object):
    def ladrar(self):
        print(""" GUAUUUU GUAAAUUU!!""")
    
    def grunir(self):
        print("""GRRRRRRRRRRR GRRRRRRRRRR""")
class Caniche(Perros):
    def ladrar(self):
        print("""guau guau guau""")

    def grunir(self):
        print("""gñññññññiiii gñññiiii""")

class Pastor_Aleman(Perros):
    def ladrar(self):
        print("""GuaUUUU  GuaUUUUU  GuaUUUUUU""")
    
    def grunir(self):
        print("Agrfgregreff aggrrfsgrrr")

class Shepadoodle (Pastor_Aleman, Caniche):
    def ladrarx(self, veces):
        for cuantas in range(veces):
            super(Shepadoodle, self).ladrar()

Tommy = Pastor_Aleman()
Piny = Caniche()
Cuchele = Shepadoodle()
Cuchele.ladrarx(5)