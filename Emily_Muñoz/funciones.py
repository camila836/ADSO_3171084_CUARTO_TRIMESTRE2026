class Cliente:   #clase
    def __init__(self, nombres, apellidos, ID, estatura, edad, saldo):   #constructor
        self.__nombres = nombres  #atributos
        self.__apellidos = apellidos
        self.__ID = ID
        self.__estatura = estatura
        self.__edad = edad
        self.__saldo = saldo

    def get_saldo(self):            #funciones
        return self.__saldo

    def set_saldo(self, nuevo_saldo):
        if isinstance(nuevo_saldo, (int, float)) and nuevo_saldo > 0:
            self.__saldo = nuevo_saldo
        else:
            print("El saldo debe ser un numero positivo.")


    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, (int)) and nueva_edad > 14:
            self.__edad = nueva_edad
        else:
          print("El cliente debe ser mayor de 14 años")


    def get_estatura(self):
         return self.__estatura

    def set_estatura(self, nueva_estatura):
        if isinstance(nueva_estatura, (int, float)) and nueva_estatura > 0:
            self.__estatura = nueva_estatura

        else:
          print("La estatura debe ser un numero positivo")




    def mostrar_todo(self):
        print(f"nombre: {self.__nombres}")
        print(f"apellidos: {self.__apellidos}")
        print(f"ID:{self.__ID}")
        print(f"estatura: {self.__estatura:,.2f}")
        print(f"edad: {self.__edad}")
        print(f"saldo: {self.__saldo:,.2f}")


def main():
    cliente1= Cliente("Emily", "Muñoz", "1023379397", 1.55, 17, 100000) #crear objeto utilizando la plantilla libro
    cliente2= Cliente("sofia", "ortega", "102837462", 1.58, 18, 150000)

    # Mostrar informacion completa
    print("Informacion completa del cliente 1:")
    cliente1.mostrar_todo()

    # Mostrar valores actuales
    print("Estatura actual:", cliente1.get_estatura())
    print("Edad actual:", cliente1.get_edad())
    print("Saldo actual:", cliente1.get_saldo())

    # Intento de actualizacion no valida
    cliente1.set_estatura(-1.80)
    cliente1.set_edad(5)
    cliente1.set_saldo(-1000)

    # Actualizacion correcta
    cliente1.set_estatura(1.58)
    cliente1.set_edad(18)
    cliente1.set_saldo(150000)

    print("Informacion completa del cliente 2:")
    cliente2.mostrar_todo()

    print("Nueva estatura despues de actualizacion:", cliente1.get_estatura())
    print("Nueva edad despues de actualizacion:", cliente1.get_edad())
    print("Nueva saldo despues de actualizacion:", cliente1.get_saldo())

    print("Programa finalizado. ")

if __name__ == "__main__":
    main()
Tú, 18 feb, 10:44 a.m.
class Libro:
  def __init__(self, titulo , precio):

    self.__Titulo = titulo 
    self.__precio = precio

  # decoradores
  # para el getter , osea los valores
  # de las variables
  @property
  def Titulo(self):
    return self.__Titulo

  @property # decorador para el getter
  def precio(self):
    return self.__precio


  @Titulo.setter
  def Titulo(self, nuevo_titulo):
    if isinstance(nuevo_titulo, str):
      self.__Titulo = nuevo_titulo
    else:
      print("Debe ingresar un valor de texto (string) para el título.")

  @precio.setter
  def precio(self, nuevo_precio):
   
    if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
      self.__precio = nuevo_precio
    else:
      print("Debe ingresar un número entero o flotante positivo para el precio.")

  def mostrar_info(self):

    print(f"El titulo del libro es: {self.__Titulo}, El precio es: ${self.__precio:,.2f}")


def main():
  print("PROGRAMA PARA VERIFICAR LOS DECORADORES EN POO @PROPERTY PARA GETTER Y @ATRIBUTO.SETTER PARA SETTER")

if __name__ == "__main__":
  main()
