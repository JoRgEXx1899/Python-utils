import os
from PyPDF2 import PdfReader, PdfWriter

def eliminar_contrasena_de_pdfs(carpeta_origen, contrasena):
    """
    Lee archivos PDF protegidos por contraseña de una carpeta,
    elimina la contraseña y los guarda en una nueva subcarpeta.

    Args:
        carpeta_origen (str): La ruta a la carpeta que contiene los PDFs.
        contrasena (str): La contraseña de los archivos PDF.
    """
    # Define el nombre de la carpeta de salida y crea la ruta completa
    carpeta_salida = os.path.join(carpeta_origen, "Procesados")

    # Crea la carpeta de salida si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
        print(f"Carpeta creada: '{carpeta_salida}'")

    # Itera sobre todos los archivos en la carpeta de origen
    for nombre_archivo in os.listdir(carpeta_origen):
        # Comprueba si el archivo es un PDF
        if nombre_archivo.lower().endswith(".pdf"):
            ruta_completa_origen = os.path.join(carpeta_origen, nombre_archivo)
            
            try:
                # Abre el archivo PDF encriptado
                lector = PdfReader(ruta_completa_origen)
                
                # Intenta desencriptar el archivo con la contraseña
                if lector.is_encrypted:
                    if lector.decrypt(contrasena):
                        print(f"Procesando archivo: '{nombre_archivo}'... ✅")
                        
                        # Crea un objeto para escribir el nuevo PDF
                        escritor = PdfWriter()
                        
                        # Copia todas las páginas del PDF original al nuevo
                        for pagina in lector.pages:
                            escritor.add_page(pagina)
                        
                        # Define la ruta del nuevo archivo sin contraseña
                        ruta_completa_salida = os.path.join(carpeta_salida, nombre_archivo)
                        
                        # Escribe el nuevo archivo PDF sin la contraseña
                        with open(ruta_completa_salida, "wb") as archivo_salida:
                            escritor.write(archivo_salida)
                            
                        print(f" -> Guardado sin contraseña en: '{ruta_completa_salida}'")
                    else:
                        print(f"Error: La contraseña para '{nombre_archivo}' es incorrecta. ❌")
                else:
                    print(f"Aviso: El archivo '{nombre_archivo}' no estaba encriptado. Se omite.")

            except Exception as e:
                print(f"No se pudo procesar el archivo '{nombre_archivo}'. Error: {e} ❌")

# --- INSTRUCCIONES DE USO ---
if __name__ == "__main__":
    # 1. Especifica la ruta a tu carpeta con los archivos PDF.
    #    Ejemplo en Windows: "C:\\Users\\TuUsuario\\Desktop\\MisPDFs"
    #    Ejemplo en macOS/Linux: "/Users/TuUsuario/Documents/PDFs"
    #    IMPORTANTE: Usa la 'r' antes de la cadena para evitar problemas con las barras invertidas.
    ruta_de_la_carpeta = r"RUTA_A_TU_CARPETA"

    # 2. Especifica la contraseña de los archivos PDF.
    tu_contrasena = "tu_contraseña_aqui"

    # Llama a la función para iniciar el proceso
    if ruta_de_la_carpeta != "RUTA_A_TU_CARPETA" and tu_contrasena != "tu_contraseña_aqui":
        eliminar_contrasena_de_pdfs(ruta_de_la_carpeta, tu_contrasena)
    else:
        print("¡CONFIGURACIÓN NECESARIA! Por favor, edita las variables 'ruta_de_la_carpeta' y 'tu_contrasena' en el script.")
