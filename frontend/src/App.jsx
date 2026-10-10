import { useState } from "react";
import { solveCube } from "./api";
import CubeInput from "./components/CubeInput";
import Cube3D from "./components/Cube3D";
import SolutionDisplay from "./components/SolutionDisplay";

const solved = { U: ["W", "W", "W", "W"], R: ["R", "R", "R", "R"], F: ["G", "G", "G", "G"], D: ["Y", "Y", "Y", "Y"], L: ["O", "O", "O", "O"], B: ["B", "B", "B", "B"] };

export default function App() {
  const [faces, setFaces] = useState(solved); const [constraint, setConstraint] = useState(""); const [result, setResult] = useState(null); const [error, setError] = useState(""); const [move, setMove] = useState("");
  async function submit(event) { event.preventDefault(); setError(""); try { const data = await solveCube({ faces, constraint }); setResult(data); data.moves.forEach((item, index) => setTimeout(() => setMove(item), index * 650)); } catch (caught) { setError(caught.message); } }
  return <main><header><p className="eyebrow">CS217C · Artificial Intelligence</p><h1>CubeVI</h1><p>Enter a 2×2×2 cube state and watch the search discover a solution.</p></header><div className="layout"><form className="panel" onSubmit={submit}><h2>Cube state</h2><CubeInput value={faces} onChange={setFaces} /><label htmlFor="constraint">Optional constraint</label><select id="constraint" value={constraint} onChange={(event) => setConstraint(event.target.value)}><option value="">No constraint</option><option value="solve it under 7 moves">Solve it under 7 moves</option><option value="find the shortest solution">Find the shortest solution</option></select><button>Solve cube</button>{error && <p className="error">{error}</p>}</form><section className="panel"><h2>Live model</h2><Cube3D move={move} /><SolutionDisplay result={result} /></section></div></main>;
}

