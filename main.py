from factory import DocumentFactory


def menu():
    print("\n=== GENERADOR DE DOCUMENTOS (FACTORY METHOD) ===")
    print("Formatos disponibles: pdf, json, csv")

    formato = input("Seleccione el formato: ")
    contenido = input("Ingrese el contenido del documento: ")

    fabrica = DocumentFactory()
    generador = fabrica.crear_generador(formato)

    resultado = generador.exportar_datos(contenido)

    print("\nResultado del sistema:")
    print(resultado)


if __name__ == "__main__":
    menu()
