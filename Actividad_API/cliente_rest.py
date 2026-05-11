import requests

def generar_informe():
    # Fase 1: URL de la API (Endpoint)
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        # Fase 2: Petición GET y captura de datos
        print("Conectando con la API...")
        respuesta = requests.get(url)
        respuesta.raise_for_status() # Verifica que la red funcione
        
        # Convertir JSON a estructura de Python (Listas/Diccionarios)
        datos = respuesta.json()
        
        # Fase 3: Procesamiento e Inteligencia Organizacional
        print("\n" + "="*50)
        print("INFORME GERENCIAL: DIRECTORIO DE COLABORADORES")
        print("="*50)
        print(f"{'NOMBRE COMPLETO':<30} | {'EMPRESA'}")
        print("-"*50)
        
        for usuario in datos:
            # Extraemos solo los campos de valor
            nombre = usuario.get('name')
            empresa = usuario.get('company', {}).get('name')
            
            print(f"{nombre:<30} | {empresa}")
            
        print("="*50)
        print("Informe generado exitosamente.\n")

    except Exception as e:
        print(f"Error en la extracción: {e}")

if __name__ == "__main__":
    generar_informe()