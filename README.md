# 🗺️ Route Mapping System Using Graph Theory

Web application designed to calculate the shortest path between rooms inside a multi-floor building using graph modeling and Dijkstra’s algorithm.

This project demonstrates applied graph theory, algorithm implementation and interactive visualization integrated with a web backend.

---

## 🏗 Architecture Overview

The system models the building as a weighted graph where:

- **Nodes** represent rooms, corridors, elevators and staircases
- **Edges** represent connections between nodes
- **Weights** represent distance or traversal cost

The backend is responsible for:

- Graph construction
- Path calculation using Dijkstra’s algorithm
- Returning structured route data to the frontend

The frontend renders the building layout and visually highlights the computed shortest path.

---

## 🔍 Core Features

- Interactive building visualization
- Multi-floor navigation
- Shortest path calculation using Dijkstra’s algorithm
- Graph modeling using NetworkX
- Dynamic route highlighting
- Web-based user interaction

---

## 🧠 Algorithmic Approach

The shortest path is computed using **Dijkstra’s algorithm**, which guarantees the optimal solution for weighted graphs without negative edges.

Flow:

1. User selects origin and destination
2. Backend retrieves graph representation
3. Dijkstra’s algorithm computes shortest path
4. Path is returned as structured data
5. Frontend renders visual route

The algorithm operates with time complexity:

O((V + E) log V)

Where:
- V = number of vertices (rooms/points)
- E = number of edges (connections)

---

## ⚙️ Tech Stack

- Python
- Flask
- NetworkX
- HTML
- CSS
- JavaScript


---

## 🚀 Running Locally

### 1. Clone repository

```bash
git clone https://github.com/JGsilvaDev/Grafos.git
cd Grafos
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start server
```bash
python app.py
```

Access:
http://localhost:5000

---

## 📌 Design Considerations
- Graph abstraction separated from presentation layer
- Clear separation between algorithm logic and UI rendering
- Weighted edges for realistic path calculation
- Scalable graph structure for future expansion
- Backend-driven computation with frontend visualization

---

## 📈 Possible Improvements
- A* algorithm implementation for heuristic optimization
- Database persistence for dynamic building layouts
- REST API refactoring
- Docker containerization
- Unit testing for graph services
- Performance benchmarking for large graphs

---

## 🎯 Purpose of the Project
This project demonstrates:
- Applied graph theory in real-world navigation
- Implementation of classical algorithms
- Backend and frontend integration
- Separation of algorithm logic from UI
- Structured problem-solving approach

It simulates a navigation system applicable to hospitals, universities or corporate buildings.

---
🤝 Contributions

Contributions and algorithmic improvements are welcome.
Feel free to open issues or submit pull requests.
