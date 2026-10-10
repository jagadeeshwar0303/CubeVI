import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { useEffect, useState } from "react";

function Model({ move }) {
  const [angle, setAngle] = useState(0);
  useEffect(() => { if (move) setAngle((value) => value + Math.PI / 2); }, [move]);
  return <group rotation={[0, angle, 0]}>{[-0.55, 0.55].flatMap((x) => [-0.55, 0.55].flatMap((y) => [-0.55, 0.55].map((z) => <mesh key={`${x}-${y}-${z}`} position={[x, y, z]}><boxGeometry args={[1, 1, 1]} /><meshStandardMaterial color="#252a31" /></mesh>)))}</group>;
}

export default function Cube3D({ move }) { return <div className="cube-stage"><Canvas camera={{ position: [3, 3, 4] }}><ambientLight intensity={1.4} /><directionalLight position={[3, 4, 5]} intensity={2} /><Model move={move} /><OrbitControls enablePan={false} /></Canvas></div>; }

