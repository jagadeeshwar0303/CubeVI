import React from "react";
import { createRoot } from "react-dom/client";

import App from "./App";
import "./styles.css";

// This is the browser entry point: mount React into the div from index.html.
createRoot(document.getElementById("root")).render(<App />);

