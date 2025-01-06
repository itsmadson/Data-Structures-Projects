
# Data Structures Course Projects


## Projects

### 1. Maze Solver
**Description**:  
This project solves a 10x10 maze using the Breadth-First Search (BFS) algorithm implemented with a `deque` data structure. The user inputs the maze as text, where:
- `S` represents the start point.
- `E` represents the end point.
- `#` represents walls.

The program visualizes the original maze and the solved path side by side.

**Features**:
- BFS algorithm for finding the shortest path.
- Interactive GUI for maze input and visualization.
- Arrows to show the direction of the solution path.
  
![Screenshot from 2025-01-06 18-59-22](https://github.com/user-attachments/assets/7b98e06f-4777-4ee7-849c-ffd5dae69896)
---

### 2. Engineering Calculator
**Description**:  
This project implements an engineering calculator using the Shunting Yard algorithm to parse and evaluate mathematical expressions. It supports basic arithmetic operations (`+`, `-`, `*`, `/`), parentheses, and decimal numbers.

**Features**:
- Shunting Yard algorithm for expression parsing.
- Error handling for invalid expressions.

![Screenshot from 2025-01-06 18-52-15](https://github.com/user-attachments/assets/074a2e92-943f-49de-a1d6-d051eff88925)
---

### 3. Heap Tree Visualization
**Description**:  
This project visualizes a max-heap data structure as a binary tree. Users can insert numbers into the heap and delete the root node. The tree is dynamically updated and displayed on the screen.

**Features**:
- Max-heap implementation with `heapify_up` and `heapify_down` functions.
- Tree visualization using `tkinter` canvas.

![Screenshot from 2025-01-06 18-53-47](https://github.com/user-attachments/assets/7cffd158-dde2-4630-b192-7a751ce45a3c)
---

### 4. Music Player
**Description**:  
This project is a music player that uses a **circular doubly linked list** to manage the playlist. Users can add, remove, and play songs, as well as navigate between tracks using previous and next buttons.

**Features**:
- Circular doubly linked list for playlist management.
- Play, pause, next, and previous functionality.
- Supports `.mp3` files.
  
![Screenshot from 2025-01-06 19-01-03](https://github.com/user-attachments/assets/d73a6657-f991-4fae-8438-76c4a4fd2691)
---
### Prerequisites
- The `tkinter` library (usually included with Python).
- The `pygame` library (for the Music Player). Install it using:
  ```bash
  pip install pygame
  ```


