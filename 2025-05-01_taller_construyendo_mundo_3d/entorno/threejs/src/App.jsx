import React from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import ModelViewer from "./ModelViewer";

function App() {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 60 }}>
      {/* Control de órbita para rotar y hacer zoom */}
      <OrbitControls target={[0, 0, 0]} />

      
      {/* Luz para que el modelo se vea bien */}
      <ambientLight intensity={0.4} />
      <directionalLight position={[5, 5, 5]} intensity={1} />
      
      {/* Componente que carga el modelo */}
      <ModelViewer />
    </Canvas>
  );
}

export default App;
