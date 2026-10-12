import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// TODO: add aliases or proxy configuration when the frontend grows.
export default defineConfig({ plugins: [react()] });

