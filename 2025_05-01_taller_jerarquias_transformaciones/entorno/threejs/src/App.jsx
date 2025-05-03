import React from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { useControls, Leva } from "leva";
import { AxesHelper } from "three";

export default function App() {
  const { rotX, rotY, rotZ, posX, posY, posZ } = useControls("Transformaciones", {
    rotX: { value: 0, min: -Math.PI, max: Math.PI },
    rotY: { value: 0, min: -Math.PI, max: Math.PI },
    rotZ: { value: 0, min: -Math.PI, max: Math.PI },
    posX: { value: 0, min: -5, max: 5 },
    posY: { value: 0, min: -5, max: 5 },
    posZ: { value: 0, min: -5, max: 5 },
  });

  return (
    <>
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
  );
}
