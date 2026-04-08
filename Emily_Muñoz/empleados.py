
import os
import sys

# Ahora es un diccionario de EMPLEADOS
empleados = {
    "001": {"nombre": "Ana", "identificacion": "123", "labor": "Cajera", "horas": 40, "salario": 5000},
    "002": {"nombre": "Luis", "identificacion": "456", "labor": "Bodega", "horas": 35, "salario": 4500},
}

nomina_actual = []

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_encabezado_tabla():
    print(f"{'ID':<6}{'NOMBRE':<15}{'IDEN':<12}{'LABOR':<15}{'HORAS':<8}{'SALARIO':<10}")
    print("-" * 70)

def mostrar_empleados():
    print("\n****** LISTA DE EMPLEADOS ******")
    if not empleados:
        print("No hay empleados registrados")
    else:
        mostrar_encabezado_tabla()
        for id_emp, datos in empleados.items():
            print(f"{id_emp:<6}{datos['nombre']:<15}{datos['identificacion']:<12}{datos['labor']:<15}{datos['horas']:<8}{datos['salario']:<10}")
    print("-" * 70)

def buscar_empleado_nombre():
    print("\n****** BUSCAR EMPLEADO ******")
    termino = input("Ingrese el nombre: ").lower()
    encontrado = False
    mostrar_encabezado_tabla()
    for id_emp, datos in empleados.items():
        if termino in datos['nombre'].lower():
            print(f"{id_emp:<6}{datos['nombre']:<15}{datos['identificacion']:<12}{datos['labor']:<15}{datos['horas']:<8}{datos['salario']:<10}")
            encontrado = True
    if not encontrado:
        print("No encontrado")

def agregar_empleado():
    print("\n****** AGREGAR EMPLEADO ******")
    id_emp = input("ID: ")
    if id_emp in empleados:
        print("Ese ID ya existe")
    else:
        nombre = input("Nombre: ")
        identificacion = input("Identificación: ")
        labor = input("Labor: ")
        try:
            horas = int(input("Horas trabajadas: "))
            salario = float(input("Pago por hora: "))
            empleados[id_emp] = {
                "nombre": nombre,
                "identificacion": identificacion,
                "labor": labor,
                "horas": horas,
                "salario": salario
            }
            print("Empleado agregado")
        except:
            print("Error en datos")

def modificar_empleado():
    mostrar_empleados()
    id_emp = input("ID a modificar: ")
    if id_emp in empleados:
        emp = empleados[id_emp]
        print("1. Cambiar horas")
        print("2. Cambiar salario por hora")
        op = input("Opción: ")

        if op == "1":
            emp["horas"] = int(input("Nuevas horas: "))
        elif op == "2":
            emp["salario"] = float(input("Nuevo salario por hora: "))
        else:
            print("Opción inválida")
    else:
        print("No existe")

def eliminar_empleado():
    mostrar_empleados()
    id_emp = input("ID a eliminar: ")
    if id_emp in empleados:
        empleados.pop(id_emp)
        print("Empleado eliminado")
    else:
        print("No encontrado")

#  MÉTODO MODIFICADO (ANTES vender_producto)
def calcular_pago():
    print("\n****** CALCULAR PAGO ******")
    mostrar_empleados()
    id_emp = input("ID del empleado: ")
    if id_emp in empleados:
        emp = empleados[id_emp]
        total = emp["horas"] * emp["salario"]
        nomina_actual.append({
            "nombre": emp["nombre"],
            "horas": emp["horas"],
            "salario": emp["salario"],
            "total": total
        })
        print(f"Pago calculado: ${total}")
    else:
        print("Empleado no encontrado")

#  MÉTODO MODIFICADO (ANTES factura)
def generar_nomina():
    print("\n****** NOMINA ******")
    total_general = 0
    for emp in nomina_actual:
        print(f"{emp['nombre']} - Horas: {emp['horas']} - Total: ${emp['total']}")
        total_general += emp['total']
    print(f"\nTOTAL A PAGAR: ${total_general}")
    nomina_actual.clear()

#  MÉTODO NUEVO 1
def empleado_mayor_pago():
    if empleados:
        mayor = max(empleados.values(), key=lambda x: x["horas"] * x["salario"])
        print(f"Empleado con mayor pago: {mayor['nombre']}")
    else:
        print("No hay empleados")

#  MÉTODO NUEVO 2
def promedio_salarios():
    if empleados:
        total = sum(emp["salario"] for emp in empleados.values())
        print(f"Promedio salario por hora: {total / len(empleados)}")
    else:
        print("No hay empleados")

def main():
    while True:
        print("\n------ SISTEMA DE EMPLEADOS ------")
        print("1. Mostrar empleados")
        print("2. Buscar empleado")
        print("3. Calcular pago")
        print("4. Generar nómina")
        print("5. Agregar empleado")
        print("6. Modificar empleado")
        print("7. Eliminar empleado")
        print("8. Empleado con mayor pago")  # nuevo
        print("9. Promedio salarios")       # nuevo
        print("10. Salir")

        opcion = input("Opción: ")

        match opcion:
            case "1": mostrar_empleados()
            case "2": buscar_empleado_nombre()
            case "3": calcular_pago()
            case "4": generar_nomina()
            case "5": agregar_empleado()
            case "6": modificar_empleado()
            case "7": eliminar_empleado()
            case "8": empleado_mayor_pago()
            case "9": promedio_salarios()
            case "10":
                break
            case _:
                print("Opción inválida")

        input("\nPresione ENTER...")
        limpiar_pantalla()

if __name__ == "__main__":
    if sys.version_info < (3, 10):
        print("Error de Python")
    else:
        main()