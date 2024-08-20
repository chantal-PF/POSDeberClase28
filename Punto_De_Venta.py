carrito = []
total = 0.0

def mostrar_menu():
    print("BIENVENIDO AL POS")
    print("1. Agregar producto al carrito")
    print("2. Eliminar producto")
    print("3. Ver total del carrito")
    print("4. Pagar")
    print("5. Salir")

def agregar_producto():
    global total 
    
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    carrito.append({"producto": producto , "precio": precio})
    total += precio
    print(f"Has agregado {producto} al carrito por {precio}.")

def eliminar_producto():
    global total
    
    producto = input("Ingrese el nombre del producto que desea eliminar: ")
    producto_eliminado = False
    
    for eliminar in carrito:
        if eliminar["producto"].lower() == producto.lower():
            carrito.remove(eliminar)
            total -= eliminar["precio"]
            print(f"Se ha eliminado {eliminar['producto']} del carrito.")
            producto_eliminado = True
            break
    
    if not producto_eliminado:
        print("El producto no se encontró en el carrito.")
  
def ver_total():
    print(f"El total de tu carrito es: {total:.2f}")
  
def pagar():
    global total , carrito 
    if total == 0:
        print("Tu carrito esta vacio, no hay nada qu pagar.")
    else:
        print(f"El total a pagar es: {total}")
        pago = float(input("Ingesa la cantidad con la que vas a pagar: "))
        if pago >= total:
            cambio = pago - total
            print(f"Pago realizado con exito: Tu cambio es: {cambio}")
         
            carrito = []
            total = 0.0
        else:
            print("No tiene suficientes dinero para pagar.")
                
def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleciona una opcion: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            ver_total()
        elif opcion == "4":
            pagar()
        elif opcion == "5":
            print("Gracias por usar el POS, ¡Hasta luego!")
            break
        else:
            print("Opcion no valida, por favor intente de nuevo.")
            
ejecutar()