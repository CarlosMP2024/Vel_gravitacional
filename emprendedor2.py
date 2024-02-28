# Versión 2

# Solicitar datos al usuario
P = float(input("Ingrese el precio de suscripción (P): "))
Unormal = int(input("Ingrese el número de usuarios normales (Unormal): "))
Upremium = int(input("Ingrese el número de usuarios premium (Upremium): "))
GT = float(input("Ingrese los gastos totales (GT): "))

# Advertir al usuario
if P <= 0 or Unormal < 0 or Upremium < 0 or GT < 0:
    print("Advertencia: Valores no válidos pueden afectar el funcionamiento del programa.")

# Calcular utilidades considerando usuarios normales y premium
utilidades = (P * Unormal + 1.5 * P * Upremium) - GT

# Mostrar resultado
print(f"Las utilidades del proyecto son: {utilidades}")
