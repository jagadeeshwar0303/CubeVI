// Keep HTTP calls in one module so React components do not know URL details.
const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function solveCube(payload) {
  // TODO: send the face arrays and optional constraint to POST /api/solve.
  // Then check response.ok and return the parsed JSON response.
  throw new Error("solveCube() is a learning TODO");
}

export async function fetchScramble(length = 6) {
  // TODO: call GET /api/scramble?length=... for a demo scramble button.
  throw new Error("fetchScramble() is a learning TODO");
}

