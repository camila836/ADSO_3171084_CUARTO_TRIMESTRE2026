class Vehiculo:
    def __init__(self, id, tipo, marca, modelo, precio):
        self.__id = id
        self.__tipo = tipo
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    # Métodos Get
    def get_id(self):
        return self.__id
    
    def get_tipo(self):
        return self.__tipo
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_precio(self):
        return self.__precio
    
    # Métodos Set
    def set_tipo(self, nuevo_tipo):
        if isinstance(nuevo_tipo, str) and nuevo_tipo.strip():
            self.__tipo = nuevo_tipo
        else:
            print("El tipo no debe quedar con espacios en blanco")

    def set_marca(self, nueva_marca):
        if isinstance(nueva_marca, str) and nueva_marca.strip():
            self.__marca = nueva_marca
        else:
            print("La marca no debe quedar con espacios en blanco")
    
    def set_modelo(self, nuevo_modelo):
        if isinstance(nuevo_modelo, str) and nuevo_modelo.strip():
            self.__modelo = nuevo_modelo
        else:
            print("El modelo no debe quedar con espacios en blanco")

    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else: 
            print("El precio debe ser mayor a 0")

    # Mostrar Información
    def mostrar_info(self):
        print(f"ID: {self.__id}, Tipo: {self.__tipo}, Marca: {self.__marca}, Modelo: {self.__modelo}, Precio: {self.__precio:.2f}")
        

def main():
    vehiculo1 = Vehiculo(1, "moto", "AKT", "2027", 8500000)
    vehiculo2 = Vehiculo(2, "avión", "vuela-vuela", "2030", 55000000)

    # Información inicial
    print("La información inicial de los vehículos es: ")
    vehiculo1.mostrar_info()
    print("-------------------")
    vehiculo2.mostrar_info()
    print("-------------------")

    # Modificación tipo
    print("Tipo actual:", vehiculo1.get_tipo(), vehiculo2.get_tipo())
    vehiculo1.set_tipo("Dirigible")
    vehiculo2.set_tipo("Submarino")
    print("Actualización del tipo del vehículo 1:", vehiculo1.get_tipo())
    print("Actualización del tipo del vehículo 2:", vehiculo2.get_tipo())
    print("-------------------")

    # Modificación marca
    print("Marca actual:", vehiculo1.get_marca(), vehiculo2.get_marca())
    vehiculo1.set_marca("Volando")
    vehiculo2.set_marca("Burbujas")
    print("Actualización de la marca del vehículo 1:", vehiculo1.get_marca())
    print("Actualización de la marca vehículo 2:", vehiculo2.get_marca())
    print("-------------------")

    # Modificación modelo
    print("Modelo actual:", vehiculo1.get_modelo(), vehiculo2.get_modelo())
    vehiculo1.set_modelo("2018")
    vehiculo2.set_modelo("2024")
    print("Actualización del modelo del vehículo 1:", vehiculo1.get_modelo())
    print("Actualización del modelo vehículo 2:", vehiculo2.get_modelo())
    print("-------------------")

    # Modificación precio
    print("Precio actual:", vehiculo1.get_precio(), vehiculo2.get_precio())
    vehiculo1.set_precio(30000000)
    vehiculo2.set_precio(500000)
    print("Actualización del precio del vehículo 1:", vehiculo1.get_precio())
    print("Actualización del precio vehículo 2:", vehiculo2.get_precio())
    print("-------------------")

    vehiculo1.mostrar_info()
    vehiculo2.mostrar_info()

if __name__ == "__main__":
    main()
