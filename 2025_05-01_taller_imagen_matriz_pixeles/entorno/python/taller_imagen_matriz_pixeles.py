# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%
# 1. Cargar imagen en color
img = cv2.imread("../../datos/el_diego.jpg")  
if img is None:
    raise ValueError("La imagen no se cargó. Verifica el nombre o ruta del archivo.")

# %%
# Convertir de BGR a RGB para visualizar con matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# %%
# 2. Acceder y mostrar los canales RGB
R, G, B = cv2.split(img_rgb)

# %%
# Convertir a HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(img_hsv)

# %%
# 3. Slicing: cambiar color en un rectángulo (ej. esquina superior izquierda)
img_mod = img_rgb.copy()
img_mod[50:150, 50:150] = [255, 0, 0]  # Rojo

# %%
# Obtener dimensiones de la imagen
height, width = img_rgb.shape[:2]

# 4. Slicing: copiar una región y pegarla en otro lugar
roi = img_rgb[50:150, 50:150].copy()

# Verificar que el área de destino esté dentro de la imagen
if 200 + roi.shape[0] <= height and 200 + roi.shape[1] <= width:
    img_mod[200:200+roi.shape[0], 200:200+roi.shape[1]] = roi
else:
    print("La región destino está fuera de los límites de la imagen.")


# %%
# 5. Calcular y mostrar histogramas de intensidades (canal V y R como ejemplo)
hist_v = cv2.calcHist([V], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([R], [0], None, [256], [0, 256])

# %%
# 6. Ajuste de brillo y contraste
# Ecuación manual: new_image = alpha * image + beta
alpha = 1.5  # Contraste
beta = 30  # Brillo
bright_contrast_manual = cv2.convertScaleAbs(img_rgb, alpha=alpha, beta=beta)

# %% [markdown]
# --- Visualización ---

# %%
fig, axes = plt.subplots(3, 4, figsize=(20, 10))
axes = axes.ravel()

# %%
axes[0].imshow(img_rgb)
axes[0].set_title("Imagen original (RGB)")

# %%
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
axes.imshow(img_rgb)
axes.set_title("Imagen original (RGB)")
axes.axis("off")
plt.show()


# %%
axes[1].imshow(R, cmap="gray")
axes[1].set_title("Canal Rojo (R)")

# %%
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
axes.imshow(R)
axes.set_title("Canal Rojo(R)")
axes.axis("off")
plt.show()


# %%
axes[2].imshow(G, cmap="gray")
axes[2].set_title("Canal Verde (G)")

# %%
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
axes.imshow(G)
axes.set_title("Canal Verde (G)")
axes.axis("off")
plt.show()


# %%
axes[3].imshow(B, cmap="gray")
axes[3].set_title("Canal Azul (B)")

# %%
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
axes.imshow(B)
axes.set_title("Canal Azul (RGB)")
axes.axis("off")
plt.show()


# %%
axes[4].imshow(H, cmap="gray")
axes[4].set_title("Canal Hue (H)")

# %%
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
axes.imshow(H)
axes.set_title("Canal Hue (H)")
axes.axis("off")
plt.show()


# %%
axes[5].imshow(S, cmap="gray")
axes[5].set_title("Canal Saturation (S)")

# %%
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
axes.imshow(S)
axes.set_title("Canal Saturation (S)")
axes.axis("off")
plt.show()


# %%
axes[6].imshow(V, cmap="gray")
axes[6].set_title("Canal Value (V)")

# %%
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
axes.imshow(V)
axes.set_title("Canal Value (V)")
axes.axis("off")
plt.show()


# %%
axes[7].imshow(img_mod)
axes[7].set_title("Modificación de regiones")

# %%
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
axes.imshow(img_mod)
axes.set_title("Modificación de regiones")
axes.axis("off")
plt.show()


# %%
axes[8].plot(hist_r, color="red")
axes[8].set_title("Histograma canal R")

# %%
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
axes.imshow(hist_r)
axes.set_title("Histograma canal R")
axes.axis("off")
plt.show()


# %%
axes[9].plot(hist_v, color="black")
axes[9].set_title("Histograma canal V")

# %%
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
axes.imshow(hist_v)
axes.set_title("Histograma canal V")
axes.axis("off")
plt.show()


# %%
axes[10].imshow(bright_contrast_manual)
axes[10].set_title("Brillo + Contraste")

# %%
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
axes.imshow(bright_contrast_manual)
axes.set_title("Brillo + Contraste")
axes.axis("off")
plt.show()


# %%
for ax in axes:
    ax.axis("off")

# %%
plt.tight_layout()
plt.show()
