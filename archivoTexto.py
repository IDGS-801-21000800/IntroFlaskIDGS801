from io import open


"""archivo = open('archivo.txt', 'a')
archivo.write("\nSaludo IDGS-801 nuevo")
archivo.close()"""

archivo = open("archivo.txt", "r")
# Lectura de archivo con cursores
"""print(archivo.read())
archivo.seek(5)
print(archivo.read())
print()"""

# Lectura de lineas de archivo 
"""print(archivo.readlines())
print()
"""
# Lectura de contenido por lineas de archivo
for datos in archivo.readlines():
    print(datos.rstrip())

archivo.close()