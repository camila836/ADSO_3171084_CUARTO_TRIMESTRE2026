def agregar_producto(lista_productos, nombre):
    # Validar nombre
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        lista_productos.append(nombre.title())
        print(f"Producto agregado: {nombre.title()}")
    else:
        print("Debe agregar un nombre válido entre 2 a 50 caracteres")


def mostrar_info(lista_productos):
    print("Lista de productos:")
    for producto in lista_productos:
        print(producto)


def modificar_producto(lista_productos, indice, nuevo_nombre):
    # Validar nombre
    if not isinstance(nuevo_nombre, str) or not (2 <= len(nuevo_nombre) <= 50):
        print("Nombre inválido. Debe tener entre 2 a 50 caracteres")
        return

    if 0 <= indice < len(lista_productos):
        original = lista_productos[indice]
        lista_productos[indice] = nuevo_nombre.title()
        print(f"Producto modificado: {original} -> {nuevo_nombre.title()}")
    else:
        print("Índice incorrecto")


def eliminar_producto(lista_productos, indice):
    if 0 <= indice < len(lista_productos):
        eliminado = lista_productos.pop(indice)
        print(f"Producto eliminado: {eliminado}")
    else:
        print("No se puede eliminar con ese índice")


def main():
    productos = ["jugo", "hueva", "queso", "arroz"]

    print("Productos actuales:")
    mostrar_info(productos)

    agregar_producto(productos, "leche")
    mostrar_info(productos)

    modificar_producto(productos, 1, "mortadela")
    mostrar_info(productos)

    eliminar_producto(productos, 2)
    mostrar_info(productos)


if __name__ == "__main__":
    main()
    
def agregar_producto(lista_productos, nombre):
    # Validar nombre
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        lista_productos.append(nombre.title())
        print(f"Producto agregado: {nombre.title()}")
    else:
        print("Debe agregar un nombre válido entre 2 a 50 caracteres")
    if not nombre.replace("", "").isalpha():
        print("El nombre solo debe contener letras")
        return
    lista_productos.append(nombre.title())
    print(f"producto agregado {nombre.title()}")
    
def mostrar_info(lista_productos):
    print("Lista de productos:")
    for producto in lista_productos:
        print(producto)


def modificar_producto(lista_productos, indice, nuevo_nombre):
    # Validar nombre
    if not isinstance(nuevo_nombre, str) or not (2 <= len(nuevo_nombre) <= 50):
        print("Nombre inválido. Debe tener entre 2 a 50 caracteres")
        return

    if 0 <= indice < len(lista_productos):
        original = lista_productos[indice]
        lista_productos[indice] = nuevo_nombre.title()
        print(f"Producto modificado: {original} -> {nuevo_nombre.title()}")
    else:
        print("Índice incorrecto")


def eliminar_producto(lista_producto, indice):
    if 0 <= indice < len(lista_producto):
        eliminado = lista_producto.pop(indice)
        print(f"Producto eliminado: {eliminado}")
    else:
        print("No se puede eliminar con ese índice")

def contar_producto(lista_productos):
    print(f"el total de productos es: {len(lista_productos)}")
      
def ordenar_producto(lista_productos):
    for producto in sorted(lista_productos):
        print("producto ordenado corectamente")
        
def main():
    producto = ["jugo", "huevo", "queso", "arroz"]

    print("Productos actuales:")
    mostrar_info(producto)

    agregar_producto(producto, "mora")
    mostrar_info(producto)

    modificar_producto(producto, 1, "atun")
    mostrar_info(producto)

    eliminar_producto(producto, 2)
    mostrar_info(producto)
    
    contar_producto(producto,)

if __name__ == "__main__":
    main()