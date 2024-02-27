import cv2
from matplotlib import pyplot as plt
import numpy as np

# Carga de la imagen y conversión de BGR a RGB
teatro = cv2.cvtColor(cv2.imread("res/Actividad2/teatro.jpg"), cv2.COLOR_BGR2RGB)

# Modificación de la imagen reduciendo la intensidad de todos los colores a la mitad
teatroModificado = (teatro * 0.5).astype(np.uint8)

# Configuración de los subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 15))
imagenes = [teatro, teatroModificado]
titulos = ['Original', 'Modificado']
colors = ['r', 'g', 'b']  # Colores para los histogramas

# Función para mostrar imagen y histograma
def mostrar_imagen_histograma(ax_imagen, ax_histograma, imagen, titulo):
    ax_imagen.imshow(imagen)
    ax_imagen.set_title(titulo)
    ax_imagen.axis('off')  # Ocultar los ejes para la imagen

    for i, color in enumerate(colors):
        ax_histograma.hist(imagen[:, :, i].ravel(), bins=256, range=(0, 255), color=color, histtype='step', density=True)
    ax_histograma.set_title(f'Histograma {titulo}')
    ax_histograma.set_xlim([0, 255])  

for i in range(2):
    mostrar_imagen_histograma(axs[i, 0], axs[i, 1], imagenes[i], titulos[i])

plt.tight_layout()
plt.show()
