import { useState } from "react";

import { solveCube } from "./api";
import Cube3D from "./components/Cube3D";
import CubeInput from "./components/CubeInput";
import SolutionDisplay from "./components/SolutionDisplay";

// TODO: use this as the initial solved form state, then add a reset button.
const SOLVED_FACES = {
  U: ["W", "W", "W", "W"], R: ["R", "R", "R", "R"],
  F: ["G", "G", "G", "G"], D: ["Y", "Y", "Y", "Y"],
  L: ["O", "O", "O", "O"], B: ["B", "B", "B", "B"],
};

export default function App() {
  // State is the bridge between child input components and the API request.
  const [faces, setFaces] = useState(SOLVED_FACES);
  const [constraint, setConstraint] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    // TODO: add loading state, call solveCube({ faces, constraint }), and show errors.
    setError("The solve workflow is a learning TODO; connect it to api.js.");
  }

  return (
    <main>
      <header>
        <p className="eyebrow">CS217C · Artificial Intelligence</p>
        <h1>CubeVI</h1>
        <p>Enter a 2×2×2 cube state and watch the search discover a solution.</p>
      </header>
      <div className="layout">
        <form className="panel" onSubmit={handleSubmit}>
          <h2>Cube state</h2>
          <CubeInput value={faces} onChange={setFaces} />
          <label htmlFor="constraint">Optional constraint</label>
          <select id="constraint" value={constraint} onChange={(event) => setConstraint(event.target.value)}>
            <option value="">No constraint</option>
            <option value="solve it under 7 moves">Solve it under 7 moves</option>
            <option value="find the shortest solution">Find the shortest solution</option>
          </select>
          <button type="submit">Solve cube</button>
          {error && <p className="error">{error}</p>}
        </form>
        <section className="panel">
          <h2>Live model</h2>
          <Cube3D />
          <SolutionDisplay result={result} />
        </section>
      </div>
    </main>
  );
}

