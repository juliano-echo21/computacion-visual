import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

# Crear un triángulo inicial (3 vértices en coordenadas homogéneas)
triangle = np.array(
    [[0, 1, 0.5], [0, 0, np.sqrt(3) / 2], [1, 1, 1]]  # Coordenadas homogéneas
)

# Directorio temporal para imágenes
if not os.path.exists("frames"):
    os.makedirs("frames")

# Número de frames y parámetros de transformación
num_frames = 60


def transform_matrix(t):
    # Escalado progresivo
    scale = 1 + 0.5 * np.sin(2 * np.pi * t)
    S = np.array([[scale, 0, 0], [0, scale, 0], [0, 0, 1]])

    # Rotación progresiva
    angle = 2 * np.pi * t
    R = np.array(
        [
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1],
        ]
    )

    # Traslación progresiva
    tx = 2 * np.cos(2 * np.pi * t)
    ty = 2 * np.sin(2 * np.pi * t)
    T = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])

    return T @ R @ S  # Orden: escalar -> rotar -> trasladar


# Crear y guardar cada frame
for i in range(num_frames):
    t = i / num_frames
    M = transform_matrix(t)
    transformed = M @ triangle

    plt.figure(figsize=(5, 5))
    x = np.append(transformed[0, :], transformed[0, 0])
    y = np.append(transformed[1, :], transformed[1, 0])

    plt.figure(figsize=(5, 5))
    plt.plot(x, y, "bo-")
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.axis("off")
    plt.savefig(f"frames/frame_{i:03d}.png")
    plt.close()


# Crear GIF con imageio
with imageio.get_writer("animated_triangle.gif", mode="I", duration=0.05) as writer:
    for i in range(num_frames):
        image = imageio.imread(f"frames/frame_{i:03d}.png")
        writer.append_data(image)

# Limpieza opcional
import shutil

shutil.rmtree("frames")
