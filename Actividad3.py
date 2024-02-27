import cv2
from matplotlib import pyplot as plt
import numpy as np

# Cargar las imágenes en escala de grises y en color
uno = cv2.imread("res/Actividad3/Uno.png", cv2.IMREAD_GRAYSCALE)
dos = cv2.imread("res/Actividad3/Dos.png", cv2.IMREAD_GRAYSCALE)
unoColor = cv2.cvtColor(cv2.imread("res/Actividad3/Uno.png"), cv2.COLOR_BGR2RGB)
dosColor = cv2.cvtColor(cv2.imread("res/Actividad3/Dos.png"), cv2.COLOR_BGR2RGB)

# Realizar operaciones en escala de grises
R = cv2.subtract(uno, dos)
uno_float = uno.astype(np.float32)
dos_float = dos.astype(np.float32)
uno_float += 10
dos_float += 10
R2 = cv2.subtract(uno_float, dos_float)
R2 = np.clip(R2, 0, 255).astype(np.uint8)  # Asegura que los valores estén en el rango correcto

# Realizar operaciones en color
RColor = cv2.subtract(unoColor, dosColor)
RColorInverso = cv2.subtract(dosColor, unoColor)

# Configurar la visualización para alta calidad
plt.figure(figsize=(20, 10))  # Ajusta el tamaño de la figura

# Mostrar las imágenes y los resultados
plt.subplot(2, 3, 1)
plt.imshow(uno, cmap='gray')
plt.title('Imagen Uno - Grayscale')

plt.subplot(2, 3, 2)
plt.imshow(dos, cmap='gray')
plt.title('Imagen Dos - Grayscale')

plt.subplot(2, 3, 3)
plt.imshow(R, cmap='gray')
plt.title('Diferencia - Grayscale')

plt.subplot(2, 3, 4)
plt.imshow(unoColor)
plt.title('Imagen Uno - Color')

plt.subplot(2, 3, 5)
plt.imshow(dosColor)
plt.title('Imagen Dos - Color')

plt.subplot(2, 3, 6)
plt.imshow(R2, cmap='gray')
plt.title('Diferencia Ajustada - Grayscale')

# Ajustar el layout para evitar la superposición
plt.tight_layout()

# Mostrar todas las imágenes en una figura
plt.show()
