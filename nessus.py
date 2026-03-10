import requests
import urllib3

# Desactivar advertencias de certificados (Nessus usa certificados locales)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# CONFIGURACIÓN
ACCESS_KEY = 'TU_API_KEY'
SECRET_KEY = 'TU_SECRET_KEY'
NESSUS_URL = "https://localhost:8834"

headers = {
    "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY}",
    "Content-Type": "application/json"
}

try:
    # Intentamos listar los escaneos creados
    response = requests.get(f"{NESSUS_URL}/scans", headers=headers, verify=False)
    
    if response.status_code == 200:
        data = response.json()
        scans = data.get('scans')
        
        if scans:
            print(f"✅ Conexión exitosa. Se han encontrado {len(scans)} escaneos en el historial.")
            for s in scans:
                print(f"- Nombre: {s['name']} | Estado: {s['status']}")
        else:
            print("✅ Conexión exitosa, pero no tienes escaneos creados todavía.")
            
    else:
        print(f"❌ Error de conexión: {response.status_code}")
        # Imprimimos la respuesta para ver si Nessus nos da más pistas
        print(f"Detalle del servidor: {response.text}")

except Exception as e:
    print(f"⚠️ Hubo un problema: {e}")