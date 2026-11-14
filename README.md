# Detector de pernos

Aplicación en Python que utiliza OpenCV y un clasificador Haar Cascade para detectar pernos en tiempo real desde una transmisión de DroidCam.

## Requisitos

- Python 3
- Un iPhone con DroidCam y una PC conectados a la misma red Wi-Fi
- El paquete `opencv-python`

Instala OpenCV con:

```bash
python -m pip install opencv-python
```

## Configuración

1. Inicia DroidCam en el iPhone y averigua la dirección IP que muestra la aplicación.
2. Abre `pernos_detector.py` y actualiza la variable `url` con esa IP. Conserva el puerto y la ruta `/4747/video`:

   ```python
   url = "http://192.168.0.13:4747/video"
   ```

3. Comprueba que el clasificador exista en `classifier/cascade.xml`.

## Ejecución

Desde la carpeta del proyecto, ejecuta:

```bash
python pernos_detector.py
```

Se abrirá una ventana con la transmisión y se dibujará un rectángulo sobre cada perno detectado. Pulsa `q` para cerrar la ventana y terminar el programa.

## Estructura del proyecto

```text
.
├── pernos_detector.py       # Captura de video y detección
├── classifier/
│   ├── cascade.xml          # Clasificador Haar entrenado
│   └── ...                  # Parámetros, etapas y registro del entrenamiento
├── p/                       # Imágenes positivas (pernos)
├── n/                       # Imágenes negativas
├── pos.lst                  # Anotaciones de imágenes positivas
├── neg.lst                  # Lista de imágenes negativas
└── pos_samples.vec          # Muestras positivas preparadas para el entrenamiento
```

El programa utiliza el clasificador ya generado; los archivos de datos y registros se incluyen como recursos del proyecto, pero `pernos_detector.py` no vuelve a entrenar el modelo.
