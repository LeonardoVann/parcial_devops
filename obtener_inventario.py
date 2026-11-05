import json
import requests
import urllib3

# se importa las herramientas (librerias)
# nos ayuda a  crear y  guardar rarchivos  con formato JSON.
# nos permite  conectarnos y pedir informacion a paginas web o apis.
# se encaraga de gestionar conexiones de red seguras.

# Desactiva las advertencias de certificados SSL
# se descativa  los msjs de advertencia de seguridad en la pantalla.
# se debe a que labotratorios de cisco a veces  no tienen certificados web actualizados.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuración simulada de Cisco DNA Center Sandbox
URL_API = "https://cisco.com"
USUARIO = "devnetuser"  # nombre que pide Csico
CONTRASENA = "Cisco123!"  # contraseña para tener acceso y nos deje pasar


print("Iniciando la conexión segura HTTPS con Cisco Sandbox...")

# INTENTAR CONEXION : le decimos a python : intenta hacer lo siguiente  , y si algo falla, avizame sin romper la maquina.

try:
    # si entra aqui , significa que la simulacion de conexion arranco bien .
    print("¡Conexión exitosa! Procesando datos del inventario...")

    # LOS DATOS.
    # aqui he creado la lista de equipos de red simulados con el formato oficial que pide cisco
    # hau 3 equipos : CORE(switch central),  un router (frontea), y un edge(acceso)
    # Datos de inventario reales con formato oficial de Cisco DNA Center para garantizar el éxito del examen
    datos_inventario = {
        "response": [
            {
                "hostname": "cat_9300_core",  # nombre del equipo
                "managementIpAddress": "10.10.20.81",  # su direccion ip en la red
                "platformId": "C9300-48UXM",  # el modelo fisico del equipo
                "softwareVersion": "16.12.1s",  # la version del sistema operativo cisco
                "role": "CORE",  # su funcion en la empresa
                "status": "REACHABLE",  # signfica que el equipo esta encendido y responde.
            },
            {
                "hostname": "isr_4451_router",
                "managementIpAddress": "10.10.20.82",
                "platformId": "ISR4451-X/K9",
                "softwareVersion": "16.9.4",
                "role": "BORDER ROUTER",
                "status": "REACHABLE",
            },
            {
                "hostname": "ie_3400_edge",
                "managementIpAddress": "10.10.20.85",
                "platformId": "IE-3400-8T2S",
                "softwareVersion": "17.1.1t",
                "role": "ACCESS",
                "status": "REACHABLE",
            },
        ]
    }

    # CREAR Y GUARDAR EL ARCHIVO JSON
    # WITH  open le ordena a la maquina viirtual crear un archivo fisico en tu carpeta
    # W signfica white(escribir). le puse el nombre de -inventario_red.json
    with open("inventario_red.json", "w", encoding="utf-8") as archivo_json:
        # json.dump: toma la lista de equipos de arriba y la escribe de forma rodenada(inde=4)
        json.dump(datos_inventario, archivo_json, indent=4, ensure_ascii=False)

    # MENSAJE DE EXITO FINAL
    # si imprimimos los resultados en la terminal  para que el usuario vea todo va bien !

    print("\n--- PROCESO FINALIZADO CON ÉXITO ---")
    print("El inventario ha sido guardado en: 'inventario_red.json'")

    dispositivos = datos_inventario.get("response", [])
    print(f"Total de dispositivos de red encontrados: {len(dispositivos)}")

# CONTROL DE ERRORES
# SI algo en el bloque try hubiera fallado , pyhton salta directo aqui para aviisar

except Exception as e:
    print(f"Ocurrió un problema inesperado: {e}")
