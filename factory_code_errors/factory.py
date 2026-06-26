class DocumentBase:
    def exportar_datos(self, datos):
        pass

# se modificaron los case

class Documento_PDF(DocumentBase):
    def exportar_datos(self, datos):
        ruta = "C:/usuarios/tu_grupo/documentos/archivo.pdf"
        print(f"\n[PDF] Guardando datos en: {ruta}")
        return f"PDF creado con éxito. Contenido: {datos}"


class Documento_JSON(DocumentBase):
    def exportar_datos(self, datos):
        ruta = "C:/usuarios/tu_grupo/documentos/archivo.json" # se creo la ruta de guardado del archivo json
        print(f"\n[JSON] Guardando datos en: {ruta}")   # se agrego la f
        return f"JSON creado con éxito. Contenido: {datos}" # se modifico el return para que devuelva un string con formato JSON
    
class Documento_CSV(DocumentBase):                           # se creo la clase csv para el formato CSV
    def exportar_datos(self, datos):                         # se creo el metodo exportar_a_csv para el formato CSV
        ruta = "C:/usuarios/tu_grupo/documentos/archivo.csv" # se creo la ruta de guardado del archivo csv
        print(f"\n[CSV] Guardando datos en: {ruta}")         # se creo el print para mostrar que se esta guardando el archivo csv
        return f"CSV creado con éxito. Contenido: {datos}"   # se creo el return para que devuelva un string con formato CSV

class DocumentFactory:
    @staticmethod
    def crear_generador(tipo_formato):
        if tipo_formato == "pdf":
            return Documento_PDF()
        elif tipo_formato == "json":
            return Documento_JSON()
        elif tipo_formato == "csv": # se agrego la condicion para el formato CSV
            return Documento_CSV() # se agrego el return para el formato CSV
