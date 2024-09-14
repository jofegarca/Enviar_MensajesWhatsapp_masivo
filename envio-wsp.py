import pandas as pd
import pywhatkit as kit
import time

# Leer el archivo Excel (asegúrate de que el archivo esté en la misma carpeta o proporciona la ruta completa)
df = pd.read_excel(r"tu-ruta\archivo")

# Iterar a través de cada fila del DataFrame
for index, row in df.iterrows():
    numero = row['Movil']  # Asegúrate de que el encabezado sea igual al de tu Excel
    mensaje = row['Mensaje']      # Asegúrate de que el encabezado sea igual al de tu Excel
    
    # Enviar el mensaje (el formato del número debe incluir el código de país, por ejemplo, +51 para Perú)
    try:
        kit.sendwhatmsg_instantly(f"+{numero}", mensaje)
        print(f"Mensaje enviado al número {numero}")
        
        # Esperar un tiempo antes de enviar el siguiente mensaje (para evitar bloqueos)
        time.sleep(7)
    
    
    except Exception as e:
        print(f"Error al enviar mensaje a {numero}: {str(e)}")