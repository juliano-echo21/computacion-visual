# 🧪 1. Transformaciones Básicas

## 📅 Fecha
`2025-05-01` 


## 🎯 Objetivo del Taller

Explorar los conceptos fundamentales de transformaciones geométricas (traslación, rotación y escala) en distintos entornos de programación visual. Las transforaciones se realizaran en funcion del tiempo

---

## 🧠 Conceptos Aprendidos

Lista los principales conceptos aplicados:

- [ ] Transformaciones geométricas (escala, rotación, traslación)

---

## 🔧 Herramientas y Entornos

Especifica los entornos usados:

- Python ( `imegeio`, `numpy`, `matplotlib`)
- Processing
- Three.js / React Three Fiber
- Jupyter / Google Colab

---

## 🧪 Implementación

### 🔹 Etapas realizadas
1. Preparación de datos y entorno.
2. Implementación de los algortimos
3. Visualización o interacción.
4. Guardado de resultados.

### 🔹 Código relevante


```python
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
```

---

## 📊 Resultados Visuales

### Python
![transformacion_basica_python](resultados/transformacion_basica_python.gif)

### Three.js

Video

### Processing

Video

---


## 💬 Reflexión Final

Responde en 2-3 párrafos:

- Aprendí a crear gifs con python. Lo que más tomó tiempo fue la grabación de los videos
