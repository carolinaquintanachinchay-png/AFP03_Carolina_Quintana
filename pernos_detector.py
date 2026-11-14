import cv2

# Ruta al clasificador Haar Cascade que entrenaste
cascade_path = 'classifier/cascade.xml'
perno_cascade = cv2.CascadeClassifier(cascade_path)

# Verificar si el modelo se cargó correctamente
if perno_cascade.empty():
    print(f"Error: No se pudo cargar el clasificador desde '{cascade_path}'. Verifica que el archivo exista dentro de la carpeta classifier.")
    exit()

# Reemplaza la IP por la que te muestra DroidCam en tu iPhone (mantén el puerto :4747/video)
url = "http://192.168.0.13:4747/video"
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error al conectar con DroidCam. Verifica que tu iPhone y tu PC estén en la misma red Wi-Fi y que la IP sea correcta.")
    exit()

print("¡Conexión exitosa con DroidCam! Iniciando detección de pernos...")
print("Presiona la tecla 'q' en la ventana de video para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo recibir el fotograma del stream de DroidCam. Reintentando...")
        break

    # Haar Cascades requiere imágenes en escala de grises para procesar la detección
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detección de pernos
    pernos = perno_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.05,
        minNeighbors=5,
        minSize=(20, 20)
    )

    # Dibujar rectángulos y etiquetas sobre los pernos encontrados
    for (x, y, w, h) in pernos:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Perno", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Mostrar la transmisión en tiempo real
    cv2.imshow('Deteccion de Pernos - DroidCam & OpenCV', frame)

    # Condición de salida: presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos de video y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()