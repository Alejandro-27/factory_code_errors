from factory import DocumentFactory

def menu():
    print(f"\n=== GENERADOR DE DOCUMENTOS (FACTORY METHOD) ===") # se agrego la f para que se muestre el mensaje en consola
    print(f"\nFormatos disponibles: pdf, json, csv") # se agrego la f y n para que se muestre el mensaje en consola y se agrego el formato csv

    formato = input("Seleccione el formato: ")
    contenido = input("Ingrese el contenido del documento: ")

    fabrica = DocumentFactory()
    generador = fabrica.crear_generador(formato)

    resultado = generador.exportar_datos(contenido)

    print(f"\nResultado del sistema:") # se agrego la f para que se muestre el mensaje en consola
    print(f"\n{resultado}") # se agrego la f y n para que se muestre el mensaje en consola

if __name__ == "__main__":
    menu()
