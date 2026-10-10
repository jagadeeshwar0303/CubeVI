# CubeVI
CubeVI is an AI-based Rubik’s Cube assistant that guides a user to solve a given randomly scrambled physical Rubik’s Cube step by step. This project is mainly a 3D simulation which presents the output as live moving steps solving the cube at the end. This project also demonstrates a few fun cube states or constraints and helps solve the Rubik’s cube.

Initial repo structure:

CubeVI/
│
├── backend/   ( python + FastAPI + pytest)
│   │
│   ├── cube/
│   │   ├── state.py
│   │   ├── moves.py
│   │   ├── validator.py
│   │   └── scramble.py
│   │
│   ├── solver/
│   │   ├── search.py
│   │   ├── heuristics.py
│   │   └── solver.py
│   │
│   ├── nlp/
│   │   └── parser.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── tests/
│   │   ├── test_cube.py
│   │   ├── test_moves.py
│   │   ├── test_solver.py
│   │   └── test_nlp.py
│   │
│   └── main.py
│
├── frontend/ (React, three.js, react three fiber)
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── Cube3D.jsx
│   │   │   ├── CubeInput.jsx
│   │   │   ├── SolutionDisplay.jsx
│   │   │   └── ConstraintInput.jsx
│   │   │
│   │   ├── App.jsx
│   │   └── api.js
│   │
│   └── package.json
│
├── README.md
└── requirements.txt
