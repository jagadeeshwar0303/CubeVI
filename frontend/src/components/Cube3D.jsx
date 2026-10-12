import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";

function CubeModel() {
  // TODO: create eight cubelets, attach coloured face stickers, and animate only
  // the layer named by the current move instead of the entire group.
  return <mesh><boxGeometry args={[2, 2, 2]} /><meshStandardMaterial color="#252a31" /></mesh>;
}

export default function Cube3D() {
  return (
    <div className="cube-stage">
      <Canvas camera={{ position: [3, 3, 4] }}>
        {/* Lighting makes the geometry readable while OrbitControls enables inspection. */}
        <ambientLight intensity={1.4} />
        <directionalLight position={[3, 4, 5]} intensity={2} />
        <CubeModel />
        <OrbitControls enablePan={false} />
      </Canvas>
    </div>
  );
}

