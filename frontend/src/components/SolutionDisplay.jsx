export default function SolutionDisplay({ result }) {
  // TODO: display depth, notation, explanation, and a step-by-step play control.
  if (!result) return <p>No solution yet.</p>;
  return <div className="result"><strong>{result.depth} moves</strong><span>{result.moves.join("  ")}</span><small>{result.explanation}</small></div>;
}

