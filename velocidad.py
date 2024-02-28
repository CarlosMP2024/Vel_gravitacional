def calcular_velocidad_escape(radio_km, gravedad):

  # Conversión de kilómetros a metros
  radio = radio_km * 1000

  # Fórmula de la velocidad de escape 
  velocidad_escape = (2 * gravedad * radio) ** 0.5

  return velocidad_escape

# Solicitud radio al usuario
radio_km = float(input("Ingrese el radio en kilómetros: "))

# Solicitud constante gravitatoria al usuario
gravedad = float(input("Ingrese la constante gravitatoria (g): "))

# Calculo de la velocidad de escape
velocidad_escape = calcular_velocidad_escape(radio_km, gravedad)

# Resultado al usuario
print(f"La velocidad de escape es {velocidad_escape:.2f} m/s")
