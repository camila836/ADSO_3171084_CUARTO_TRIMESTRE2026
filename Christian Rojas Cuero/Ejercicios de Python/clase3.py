class Vehiculo: #CLase padre
    def mover(self):
        print("==== Vehiculo se esta moviendo ====")

class Carro(Vehiculo): #Clase hija
    def mover(self):
        print("==== El carro se mueve por la carretera ====")
class Moto(Vehiculo):
    def mover(self):
        print("==== La moto va mil por la autopista ====")
class Avion(Vehiculo):
    def mover(self):
        print("====El avion vuela sobre las nuves====")
class Submarino(Vehiculo):
    pass
    def mover(self):
        print("==== El submarino bucea por bolivia ===")
def main():
    
    print("Ahora utilizaremos en metodo mover() pero desde el hijo")
    print("Vamos a heredar este metodo desde carro")
    carro1 = Carro()
    carro1.mover()
    moto1 = Moto()
    print("Metodo mover reutilizado desde moto hijo")
    moto1.mover()
    avion1 = Avion()
    avion1.mover()
    submarino = Submarino()
    submarino.mover()

if __name__ == "__main__":
        main()