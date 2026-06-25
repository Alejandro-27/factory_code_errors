class DocumentBase:
    def exportar_datos(self, datos):
        pass


class documento_pdf(DocumentBase):
    def exportar_datos(self, datos):
        ruta = "C:/usuarios/tu_grupo/documentos/archivo.pdf"
        print(f"\n[PDF] Guardando datos en: {ruta}")
        return f"PDF creado con éxito. Contenido: {datos}"


class DocumentoJSON(DocumentBase):
    def exportar_a_json(self, datos):
        print("\n[JSON] Formateando estructura...")
        return f'{{"datos": "{datos}"}}'


class DocumentFactory:
    @staticmethod
    def crear_generador(tipo_formato):
        if tipo_formato == "pdf":
            return documento_pdf()
        elif tipo_formato == "json":
            return DocumentoJSON()
