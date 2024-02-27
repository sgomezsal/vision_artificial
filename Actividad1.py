import cv2
from matplotlib import pyplot as plt
import numpy as np

# Carga de la imagen y conversión de BGR a RGB
img_original = cv2.cvtColor(cv2.imread('res/Actividad1/bacteria.jpeg'), cv2.COLOR_BGR2RGB)
img_negativo = 255 - img_original

# Configuración de los subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 15))
titles = ['Original', 'Histograma Original', 'Negativo', 'Histograma Negativo']
functions = [lambda ax, img: ax.imshow(img), lambda ax, img: ax.hist([img[:, :, i].ravel() for i in range(3)], bins=256, color=['r', 'g', 'b'], histtype='step', density=True)]

# Iteración a través de las configuraciones de subplots para mostrar imágenes y histogramas
for i, (ax, img) in enumerate(zip(axes.flatten(), [img_original, img_original, img_negativo, img_negativo])):
    if i % 2 == 0:  # Imágenes
        functions[0](ax, img)
    else:  # Histogramas
        functions[1](ax, img)
    ax.set_title(titles[i])

plt.tight_layout()
plt.show()
