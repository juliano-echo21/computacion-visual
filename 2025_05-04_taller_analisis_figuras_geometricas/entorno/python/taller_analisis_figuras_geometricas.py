import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# 1. Cargar imagen y convertir a escala de grises
img = cv2.imread("../../datos/formas.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Binarizar
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 3. Encontrar contornos
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4. Crear lista de cuadros para GIF
frames = []
img_copy = img.copy()

for i, cnt in enumerate(contours):
    # Calcular área y perímetro
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)

    # Calcular centroide
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 0, 0

    # Aproximar contorno para identificar figura
    approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
    vertices = len(approx)
    if vertices == 3:
        shape = "Triángulo"
    elif vertices == 4:
        shape = "Cuadrado"
    elif vertices > 4:
        shape = "Círculo"
    else:
        shape = "Desconocida"

    # Dibujar contorno
    cv2.drawContours(img_copy, [cnt], -1, (0, 255, 0), 2)
    # Dibujar centroide y texto
    text = f"{shape}\nA={int(area)} P={int(perimeter)} C=({cx},{cy})"
    cv2.putText(
        img_copy, text, (cx - 50, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1
    )

    # Guardar frame para GIF
    bgr_frame = cv2.cvtColor(img_copy.copy(), cv2.COLOR_BGR2RGB)
    pil_frame = Image.fromarray(bgr_frame)
    frames.append(pil_frame)

# Guardar GIF
frames[0].save(
    "shapes_detected.gif", save_all=True, append_images=frames[1:], duration=600, loop=0
)

# Mostrar última imagen
plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
plt.title("Contornos y métricas detectadas")
plt.axis("off")
plt.show()
