
# Proyecto de Procesamiento de Imágenes

## Descripción General
Este proyecto consiste en una serie de scripts de Python diseñados para realizar operaciones de procesamiento de imágenes. Las actividades incluidas abarcan la manipulación de imágenes, análisis de histogramas y operaciones entre imágenes, utilizando principalmente la librería OpenCV y Matplotlib.

## Requisitos y Dependencias
Antes de ejecutar los scripts, asegúrese de tener instalado Python 3 y las siguientes bibliotecas:
- OpenCV (cv2)
- Matplotlib
- NumPy

Puede instalar todas las dependencias necesarias utilizando el siguiente comando:
```bash
pip install opencv-python-headless matplotlib numpy
```

## Instrucciones de Instalación
Para utilizar estos scripts, siga los siguientes pasos:
1. Clone el repositorio o descargue los archivos en su máquina local.
2. Asegúrese de que todas las dependencias estén instaladas.
3. Guarde las imágenes necesarias en las carpetas correspondientes dentro de `res/Actividad1/`, `res/Actividad2/` y `res/Actividad3/` según corresponda.

## Uso de los Scripts
1. **Actividad1.py**: Este script realiza la conversión de una imagen a su negativo y muestra el histograma de ambas imágenes.
   - Ejecute el script con `python Actividad1.py`.
   - Asegúrese de que `res/Actividad1/bacteria.jpeg` exista.

2. **Actividad2.py**: Este script reduce la intensidad de todos los colores a la mitad en una imagen y compara el resultado con la imagen original, mostrando ambos histogramas.
   - Ejecute el script con `python Actividad2.py`.
   - Asegúrese de que `res/Actividad2/teatro.jpg` exista.

3. **Actividad3.py**: Este script realiza operaciones entre dos imágenes, mostrando las diferencias en escala de grises y en color.
   - Ejecute el script con `python Actividad3.py`.
   - Asegúrese de que `res/Actividad3/Uno.png` y `res/Actividad3/Dos.png` existan.

Asegúrese de estar en el directorio correcto cuando ejecute los scripts y de que las imágenes requeridas estén en sus respectivas carpetas. Los resultados se mostrarán en ventanas de visualización de Matplotlib.

## Notas Adicionales
- Puede modificar las rutas de las imágenes dentro de los scripts para probar con diferentes imágenes.
- Ajuste la configuración de visualización de Matplotlib según sea necesario para adaptarla a su entorno de visualización.
