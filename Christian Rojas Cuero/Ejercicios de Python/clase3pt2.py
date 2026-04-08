class Padre():
    def __init__(self, mensaje):
        self.mensaje = mensaje
class Hijo(Padre):
    def __init__(self, mensaje, nombre):
        super().__init__(mensaje)
        self.nombre = nombre

def main():

    objecto1 = Hijo ("Este mensaje desde la clase padre", "Este mensaje desde la clase hijo")
    print(f"{objecto1.mensaje}, {objecto1.nombre}")
    print(objecto1.mensaje)
    print(objecto1.nombre)
if __name__ == "__main__":
    main()