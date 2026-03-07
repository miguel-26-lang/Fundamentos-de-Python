
# Función para validar texto (no vacío, no solo espacios)
def leer_texto(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato == "":
            print("Error: no se permite dejar el campo vacío.")
        elif not dato.replace(" ", "").isalpha():
            print("Error: solo se permiten letras.")
        else:
            return dato


# Función para validar entero (edad)
def leer_entero(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato == "":
            print("Error: no se permite dejar el campo vacío.")
        else:
            try:
                valor = int(dato)
                if valor <= 0:
                    print("Error: debe ser un número positivo.")
                else:
                    return valor
            except ValueError:
                print("Error: debe ingresar un número entero válido.")


# Función para validar decimal (peso y estatura)
def leer_decimal(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato == "":
            print("Error: no se permite dejar el campo vacío.")
        else:
            try:
                valor = float(dato)
                if valor <= 0:
                    print("Error: debe ser un número mayor que cero.")
                else:
                    return valor
            except ValueError:
                print("Error: debe ingresar un número válido (decimal o entero).")


# Programa principal
nombre = leer_texto("Proporcionar el nombre: ")
nombre = nombre.title()
apell_pat = leer_texto("Proporcionar el apellido paterno: ")
apell_pat = apell_pat.title()
apell_mat = leer_texto("Proporcionar el apellido materno: ")
apell_mat = apell_mat.title()

edad = leer_entero("Proporcionar la edad: ")
peso = leer_decimal("Proporcionar el peso (kg): ")
estatura = leer_decimal("Proporcionar la estatura (m): ")

print("\n--- DATOS CAPTURADOS ---")
print("Nombre:", nombre)
print("Apellido paterno:", apell_pat)
print("Apellido materno:", apell_mat)
print("Edad:", edad)
print("Peso:", peso)
print("Estatura:", estatura)

IMC = peso / estatura ** 2
print("\nEl IMC de", nombre, apell_pat, apell_mat, "es de:", round(IMC, 2), "kg/m²")

if IMC < 18.5:
    print("Bajo peso y Riesgo de desnutrición")
elif IMC <= 24.9:
    print("Peso normal y Estado nutricional adecuado")
elif IMC <= 29.9:
    print("Sobrepeso / Exceso de peso corporal")
elif IMC <= 34.9:
    print("Obesidad grado I / Obesidad leve")
elif IMC <= 39.9:
    print("Obesidad grado II / Obesidad moderada")
else:
    print("Obesidad grado III / Obesidad severa o mórbida")
