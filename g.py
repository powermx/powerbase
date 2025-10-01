import sys
from googlesearch import search

# Verifica si hay un argumento de búsqueda
if len(sys.argv) < 2:
    print("Por favor ingresa una consulta de búsqueda.")
    sys.exit(1)

# Obtiene la consulta de búsqueda desde los argumentos de la línea de comandos
query = " ".join(sys.argv[1:])  # Une los argumentos para formar la consulta completa

# Añadir "wotlk" al final de la consulta
query += " wotlk"

# Realiza la búsqueda en Google y limita los resultados a los 2 primeros
results = search(query, num_results=2, advanced=True)

# Itera sobre los resultados y muestra la información sin los separadores
for result in results:
    print("---------------")
    print(f"Title: {result.title}")
    print(f"URL: {result.url}")
    print(f"Description: {result.description}")
    print("---------------")
