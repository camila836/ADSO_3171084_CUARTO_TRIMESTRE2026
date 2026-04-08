class Libro:   #clase
    def __init__(self, titulo, precio):   #constructor
        self.__titulo = titulo  #atributos
        self.__precio = precio

    def get_precio(self):            #funciones
        return self.__precio

    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser un numero positivo.")

    def mostrar_info(self):
        print(f"\nTitulo: {self.__titulo}")
        print(f"Precio: {self.__precio:,.2f}")
        print("--------------------")
        print(f"Titulo: {self.__titulo}, precio {self.__precio:,.2f}\n")

def main():
    libro1 = Libro("Python Profesional", 120000) #crear objeto utilizando la plantilla libro
    libro2 = Libro("Java Profesional", 150000)

    # Mostrar informacion inicial
    print("Informacion inicial del libro:")
    libro1.mostrar_info()

    # Mostrar precio actual
    print("Precio actual:", libro1.get_precio())

    # Intento de actualizacion no valida
    libro1.set_precio(-10)

    # Actualizacion correcta
    libro1.set_precio(150000)

    print("Nuevo precio despues de actualizacion:", libro1.get_precio())

    print("Programa finalizado. ")

if __name__ == "__main__":
    main()
