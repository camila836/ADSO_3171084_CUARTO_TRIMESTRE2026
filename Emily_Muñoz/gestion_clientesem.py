
def agregar_Clientes(lista_clientes, nombre):
    #Validacion de la longitud de un cliente
    #Verifica que el nombre sea una cadena de longitud entre 2 a 50 caracteres
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        #Si valido colocaremos el primer caracter en mayuscula
        lista_clientes.append(nombre.title())
        #Mostraremos un mensaje indicando que el cliente fue agregado
        print(f"Cliente agregado: {nombre.title()}")
    else:
        print("Debe agregar un nombre valido entre 2 a 50 caracteres.")


#Imprimiremos todos los clientes registrados en las lista_clientes
def mostrar_Clientes(lista_clientes):
  for cliente in lista_clientes:
    print(f"{cliente}")
    
def modificar_Clientes(lista_clientes, indice, nuevo_nombre):
    #modificaremos el nombre de un cliente en la lista
    if not isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50:
        print("Nombre de cliente invalido debe tener entre 2 y 50 caracteres")
        return
    if 0 <= indice < len(lista_clientes):
    #guardaremos el nombre original de la lista antes de modificar el (original)
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"Cliente modificado {original} por -> {nuevo_nombre.title()}")
    else: 
        print("No existe ese dato en la lista o indice incorrecto.")
def eliminar_cliente(lista_clientes, indice):
    #eliminaremos el cliente indicando la posicion en la lista
    if 0 <= indice < len(lista_clientes):
        eliminado= lista_clientes.pop(indice)
        #Mostraremos un mensaje confirmando la eliminacion de ese dato en la lista
        print(f"Cliente eliminado: {eliminado}")
    else: 
       print ("No se puede eliminar el cliente con ese indice fuera de rango")
       
def main():
    clientes = ["ana", "marcos", "beatriz"]
    print("Clientes actuales")
    mostrar_Clientes(clientes)
    # agregaremos un cliente nuevo
    print("agregar un cliente")
    agregar_Clientes(clientes, "marcos")
    mostrar_Clientes(clientes)
    # modificar un cliente
    print("modificar cliente")
    modificar_Clientes(clientes,1,"Jhon")
    mostrar_Clientes(clientes)
    # eliminaremos un cliente
    print("eliminar cliente")
    eliminar_cliente(clientes,2)
    mostrar_Clientes(clientes)
if __name__ == "__main__":
   main()