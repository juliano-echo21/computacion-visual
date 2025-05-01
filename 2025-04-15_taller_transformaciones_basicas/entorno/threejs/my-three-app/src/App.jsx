import { Canvas, useFrame, useThree } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { useRef } from 'react'

function AnimatedObject() {
  const meshRef = useRef()
  const { clock } = useThree()

  useFrame(() => {
    const t = clock.getElapsedTime()

    // Movimiento circular
    meshRef.current.position.x = Math.cos(t) * 2
    meshRef.current.position.y = Math.sin(t) * 2

    // Rotación
    meshRef.current.rotation.x += 0.01
    meshRef.current.rotation.y += 0.01

    // Escala pulsante
    const scale = 1 + 0.3 * Math.sin(t * 2)
    meshRef.current.scale.set(scale, scale, scale)
  })

  return (
    <mesh ref={meshRef}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color='royalblue' />
    </mesh>
  )
}

function App() {
  return (
    <Canvas camera={{ position: [0, 0, 5] }}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 5, 5]} />
      <OrbitControls />
      <AnimatedObject />
    </Canvas>
  )
}

export default App
