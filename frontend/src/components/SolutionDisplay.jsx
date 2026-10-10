export default function SolutionDisplay({ result }) { return result && <div className="result"><strong>{result.depth} moves</strong><span>{result.moves.join("  ") || "Already solved"}</span><small>{result.explanation}</small></div>; }

