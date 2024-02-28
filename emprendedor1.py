# Versión 1

# Solicitar datos al usuario
P = float(input("Ingrese el precio de suscripción (P): "))
U = int(input("Ingrese el número de usuarios (U): "))
GT = float(input("Ingrese los gastos totales (GT): "))

# Advertir al usuario
if P <= 0 or U <= 0 or GT < 0:
    print("Advertencia: Valores no válidos pueden afectar el funcionamiento del programa.")

# Calculo de utilidades
utilidades = P * U - GT

# Mostrar resultado
print(f"Las utilidades del proyecto son: {utilidades}")
