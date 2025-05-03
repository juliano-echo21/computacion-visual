import React from "react";
import { useGLTF, Edges, Points, PointMaterial } from "@react-three/drei";

export default function ModelViewer() {
  // Cargar modelo GLTF (puedes usar también useSTL o useLoader para .OBJ/.STL)
  const { nodes, scene } = useGLTF("/silla.gltf");

  return (
    <group>
      {/* Visualizar el modelo base */}
      <primitive object={scene}  />

      {/* Mostrar aristas con líneas */}
      <Edges
        geometry={scene.children[0].geometry} // Primera malla del modelo
        scale={1.01} // Ligeramente más grande para evitar solapamiento visual
        threshold={15} // Ángulo para detectar aristas duras
        color="black"
      />

      {/* Mostrar vértices como puntos */}
      <Points
        geometry={scene.children[0].geometry}
        scale={1.02}
      >
        <PointMaterial
          color="red"
          size={0.02}
          sizeAttenuation
          depthWrite={false}
        />
      </Points>
    </group>
  );
}
