const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
export async function solveCube(payload) {
  const response = await fetch(`${API_URL}/api/solve`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) });
  const data = await response.json();
  if (!response.ok) throw new Error(data.detail || "Unable to solve cube");
  return data;
}

