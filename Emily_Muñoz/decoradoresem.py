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