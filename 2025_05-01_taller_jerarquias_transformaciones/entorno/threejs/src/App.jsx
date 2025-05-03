import React, { useState } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Box } from "@react-three/drei";
import { Leva } from "leva";

export default function App() {
  // Estado para controlar la rotación y la traslación
  const [rotation, setRotation] = useState({ x: 0, y: 0, z: 0 });
  const [translation, setTranslation] = useState({ x: 0, y: 0, z: 0 });

  return (
    <>
      {/* Interface de control con leva */}
      <Leva
        flat
        title="Transformaciones"
        values={{
          "Padre Rotación X": { value: rotation.x, min: -Math.PI, max: Math.PI },
          "Padre Rotación Y": { value: rotation.y, min: -Math.PI, max: Math.PI },
          "Padre Rotación Z": { value: rotation.z, min: -Math.PI, max: Math.PI },
          "Padre Traslación X": { value: translation.x, min: -5, max: 5 },
          "Padre Traslación Y": { value: translation.y, min: -5, max: 5 },
          "Padre Traslación Z": { value: translation.z, min: -5, max: 5 },
        }}
        onChange={(values) => {
          setRotation({ x: values["Padre Rotación X"], y: values["Padre Rotación Y"], z: values["Padre Rotación Z"] });
          setTranslation({ x: values["Padre Traslación X"], y: values["Padre Traslación Y"], z: values["Padre Traslación Z"] });
        }}
      />
      
      {/* Canvas de Three.js con la escena */}
      <Canvas>
        {/* Luz para iluminar la escena */}
        <ambientLight intensity={0.5} />
        <directionalLight position={[5, 5, 5]} intensity={1} />

        {/* Grupo padre */}
        <group position={[translation.x, translation.y, translation.z]} rotation={[rotation.x, rotation.y, rotation.z]}>
          {/* Primer nivel de malla hijo */}
          <mesh position={[-2, 0, 0]} rotation={[rotation.x, rotation.y, rotation.z]}>
            <boxGeometry args={[1, 1, 1]} />
            <meshStandardMaterial color="red" />
          </mesh>

          {/* Segundo nivel de malla hijo */}
          <group position={[2, 0, 0]}>
            <mesh rotation={[rotation.x, rotation.y, rotation.z]}>
              <boxGeometry args={[1, 1, 1]} />
              <meshStandardMaterial color="green" />
            </mesh>

            {/* Tercer nivel de malla hijo */}
            <group position={[2, 0, 0]}>
              <mesh rotation={[rotation.x, rotation.y, rotation.z]}>
                <boxGeometry args={[1, 1, 1]} />
                <meshStandardMaterial color="blue" />
              </mesh>
            </group>
          </group>
        </group>

        {/* Controles para mover y rotar la cámara */}
        <OrbitControls />
      </Canvas>
    </>
  );
}
