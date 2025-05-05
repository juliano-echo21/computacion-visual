import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar imagen en color
img = cv2.imread("../../datos/el_diego.jpg")
if img is None:
    raise ValueError("La imagen no se cargó. Verifica el nombre o ruta del archivo.")

# Convertir de BGR a RGB para visualizar con matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2. Acceder y mostrar los canales RGB
R, G, B = cv2.split(img_rgb)

# Convertir a HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(img_hsv)

# 3. Slicing: cambiar color en un rectángulo (ej. esquina superior izquierda)
img_mod = img_rgb.copy()
img_mod[50:150, 50:150] = [255, 0, 0]  # Rojo

# 4. Slicing: copiar una región y pegarla en otro lugar
height, width = img_rgb.shape[:2]
roi = img_rgb[50:150, 50:150].copy()
if 200 + roi.shape[0] <= height and 200 + roi.shape[1] <= width:
    img_mod[200 : 200 + roi.shape[0], 200 : 200 + roi.shape[1]] = roi
else:
    print("La región destino está fuera de los límites de la imagen.")

# 5. Calcular histogramas (usaremos matplotlib para histogramas de R y V)
# Histograma canal R
plt.figure(figsize=(6, 4))
plt.hist(R.ravel(), bins=256, range=[0, 256], color="red")
plt.title("Histograma canal R")
plt.xlabel("Intensidad")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

# Histograma canal V
plt.figure(figsize=(6, 4))
plt.hist(V.ravel(), bins=256, range=[0, 256], color="black")
plt.title("Histograma canal V")
plt.xlabel("Intensidad")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

# 6. Ajuste de brillo y contraste
alpha = 1.5  # Contraste
beta = 30  # Brillo
bright_contrast_manual = cv2.convertScaleAbs(img_rgb, alpha=alpha, beta=beta)


# Visualización independiente de cada imagen
def show_image(image, title, cmap=None):
    plt.figure(figsize=(6, 6))
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.show()


# Mostrar imágenes individuales
show_image(img_rgb, "Imagen original (RGB)")
show_image(R, "Canal Rojo (R)", cmap="gray")
show_image(G, "Canal Verde (G)", cmap="gray")
show_image(B, "Canal Azul (B)", cmap="gray")
show_image(H, "Canal Hue (H)", cmap="gray")
show_image(S, "Canal Saturation (S)", cmap="gray")
show_image(V, "Canal Value (V)", cmap="gray")
show_image(img_mod, "Modificación de regiones")
show_image(bright_contrast_manual, "Brillo + Contraste")
