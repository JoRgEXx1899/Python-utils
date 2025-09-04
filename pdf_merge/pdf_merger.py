import os
from PyPDF2 import PdfMerger

def unir_pdfs_en_carpeta(carpeta_origen,nombre_salida=None):
    """
    Busca todos los archivos PDF en una carpeta, los ordena y los une
    en un único archivo PDF de salida.

    Args:
        carpeta_origen (str): La ruta a la carpeta que contiene los PDFs.
    """
    # Crea un objeto para fusionar los PDFs
    fusionador = PdfMerger()

    # Lista para almacenar las rutas de los PDFs encontrados
    lista_de_pdfs = []

    # Busca todos los archivos .pdf en la carpeta de origen
    for nombre_archivo in os.listdir(carpeta_origen):
        if nombre_archivo.lower().endswith(".pdf"):
            lista_de_pdfs.append(os.path.join(carpeta_origen, nombre_archivo))
    
    # Ordena los archivos alfabéticamente para unirlos en un orden predecible
    lista_de_pdfs.sort()

    if not lista_de_pdfs:
        print("❌ No se encontraron archivos PDF en la carpeta especificada.")
        return

    print("Se unirán los siguientes archivos en este orden:")
    for pdf in lista_de_pdfs:
        print(f"  -> {os.path.basename(pdf)}")

    # Agrega cada archivo PDF al objeto fusionador
    for ruta_pdf in lista_de_pdfs:
        fusionador.append(ruta_pdf)

    # Genera el nombre del archivo de salida
    if (nombre_salida==None):
        primer_archivo_nombre = os.path.basename(lista_de_pdfs[0])
        prefijo = primer_archivo_nombre[:4]
        nombre_salida = f"Consolidado {prefijo}.pdf"
    ruta_salida = os.path.join(carpeta_origen, nombre_salida)

    try:
        # Escribe el PDF fusionado en el archivo de salida
        with open(ruta_salida, "wb") as archivo_final:
            fusionador.write(archivo_final)
        
        print(f"\n✅ ¡Éxito! Archivos unidos correctamente en: '{ruta_salida}'")

    except Exception as e:
        print(f"\n❌ Ocurrió un error al crear el archivo consolidado: {e}")

    finally:
        # Cierra el objeto fusionador
        fusionador.close()


# --- INSTRUCCIONES DE USO ---
if __name__ == "__main__":
    # 1. Especifica la ruta a la carpeta donde están los PDFs que quieres unir.
    #    Ejemplo en Windows: r"C:\Users\TuUsuario\Desktop\Reportes"
    #    Ejemplo en macOS/Linux: r"/Users/TuUsuario/Documents/Facturas"
    #    IMPORTANTE: Usa la 'r' antes de la cadena para evitar problemas con las barras invertidas.
    ruta_a_la_carpeta = r"RUTA_A_TU_CARPETA"

    # Llama a la función para iniciar el proceso
    if ruta_a_la_carpeta != "RUTA_A_TU_CARPETA":
        unir_pdfs_en_carpeta(ruta_a_la_carpeta)
    else:
        print("¡CONFIGURACIÓN NECESARIA! Por favor, edita la variable 'ruta_a_la_carpeta' en el script.")