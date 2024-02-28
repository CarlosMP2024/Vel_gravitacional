# Versión 3

# Solicitar datos al usuario
P = float(input("Ingrese el precio de suscripción (P): "))
U = int(input("Ingrese el número de usuarios (U): "))
GT = float(input("Ingrese los gastos totales (GT): "))
Uanterior = float(input("Ingrese las utilidades del año anterior (Uanterior): "))

# Advertir al usuario
if P <= 0 or U <= 0 or GT < 0 or Uanterior < 0:
    print("Advertencia: Valores no válidos pueden afectar el funcionamiento del programa.")

# Calcular utilidades actuales
utilidades_actuales = P * U - GT

# Calcular la razón entre las utilidades actuales y las del año anterior
razon_utilidades = utilidades_actuales / Uanterior

# Mostrar resultado
print(f"Las utilidades del proyecto son: {utilidades_actuales}")
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon_utilidades:.2f}")
