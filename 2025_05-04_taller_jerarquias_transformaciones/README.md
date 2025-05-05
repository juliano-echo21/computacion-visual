# 🧪 2. Jerarquías y Transformaciones: El Árbol del Movimiento

## 📅 Fecha
`2025-05-03` 


## 🎯 Objetivo del Taller

Aplicar estructuras jerárquicas y árboles de transformación para organizar escenas y simular movimiento relativo entre objetos. Se busca comprender cómo las transformaciones afectan a los nodos hijos en una estructura padre-hijo y cómo visualizar estos efectos en tiempo real.

---

## 🧠 Conceptos Aprendidos

Lista los principales conceptos aplicados:

- estructura padre-hijo
- efectos en tiempo real.
---

## 🔧 Herramientas y Entornos

Especifica los entornos usados:

- Three.js / React Three Fiber (`OrbitControls`,`Leva`,`AxesHelper`)

---

## 🧪 Implementación

### 🔹 Etapas realizadas
1. Preparación de datos y entorno.
2. Implementación de los algortimos
3. Visualización o interacción.
4. Guardado de resultados.

### 🔹 Código relevante

### Código Threejs
```python
<Leva />
      <Canvas camera={{ position: [5, 5, 5], fov: 60 }}>
        <ambientLight intensity={0.5} />
        <directionalLight position={[5, 5, 5]} />
        <OrbitControls />
        <primitive object={new AxesHelper(5)} />

        {/* Nodo padre */}
        <group rotation={[rotX, rotY, rotZ]} position={[posX, posY, posZ]}>
          {/* Hijo: cubo */}
          <mesh position={[2, 0, 0]}>
            <boxGeometry />
            <meshStandardMaterial color="orange" />
            <primitive object={new AxesHelper(2)} />

            {/* Nieto: esfera */}
            <mesh position={[1.5, 1.5, 0]}>
              <sphereGeometry args={[0.4, 32, 32]} />
              <meshStandardMaterial color="limegreen" />
              <primitive object={new AxesHelper(1)} />
            </mesh>
          </mesh>
        </group>
      </Canvas>
    </>
```

## 📊 Resultados Visuales


### Three.js

![Estructura padre hijo](datos/jerarquia.mp4)

---

## 💬 Reflexión Final

La librería Leva me pareció muy completa e interactiva. Bastante versátil y util.