import sys
import os
import requests
import json
import time
# Verificar que se pase el archivo como argumento
if len(sys.argv) != 2:
    print("Uso: python email.py <archivo_emails.txt>")
    sys.exit(1)

# Obtener el nombre del archivo de correos electrónicos desde los argumentos
correos_filename = sys.argv[1]

# Verificar que el archivo de correos electrónicos existe
if not os.path.isfile(correos_filename):
    print(f"El archivo {correos_filename} no existe.")
    sys.exit(1)

# Leer el archivo de correos electrónicos
def leer_correos(filename):
    with open(filename, 'r') as file:
        correos = file.readlines()
    # Eliminar espacios en blanco y saltos de línea
    correos = [correo.strip() for correo in correos]
    return correos

# Hacer solicitud a la API y obtener resultados
def obtener_resultados(correo, retries=3, delay=2):
    url = f"https://api.breachdirectory.org/rapidapi-IscustemTaingtowItrionne?func=auto&term={correo}"
    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)
            # Esperar 1 segundo antes de hacer la siguiente solicitud
            #time.sleep(delay)
            response.close()
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error al hacer la solicitud para {correo}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error de red para {correo}: {e}")
            time.sleep(delay * (i + 1))  # Pausa exponencial
    return None

# Guardar resultados en un archivo JSON
def guardar_resultados(resultados, filename):
    with open(filename, 'w') as file:
        json.dump(resultados, file, indent=4)

# Función principal
def main(correos_filename):
    correos = leer_correos(correos_filename)
    todos_los_resultados = []

    for correo in correos:
        resultado = obtener_resultados(correo)
        if resultado and resultado.get("success") and resultado.get("found", 0) > 0:
            entrada = {
                "correo": correo,
                "resultados": resultado["result"]
            }
            todos_los_resultados.append(entrada)

    # Guardar los resultados en un archivo JSON con el mismo nombre que el archivo de correos pero con extensión .json
    resultados_filename = os.path.splitext(correos_filename)[0] + ".json"
    guardar_resultados(todos_los_resultados, resultados_filename)
    print(f"Resultados guardados en {resultados_filename}")

# Llamar a la función principal
if __name__ == "__main__":
    main(correos_filename)
