def datos_valentina():
 print("Mi nombre es Valentina y tengo 22 años.")

def datos_random():
 print("Mi nombre es Random y tengo ? años.")

# Menú base del programa
while True:
 print("\n--- MENÚ PRINCIPAL ---")
 print("1. Función de integrante 1")
 print("2. Función de integrante 2")
 print("3. Función de integrante 3")
 print("0. Salir")
 op = input("Seleccione opción: ")
 if op == "0":
    print("Programa finalizado.")
    break
 elif op == "1":
    datos_valentina()
 elif op == "2":
    datos_random()
 elif op == "3":
    pass # Aquí se llamará a la función del integrante 3
 else:
    print(" Opción inválida.")
