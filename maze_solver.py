import tkinter as tk
from collections import deque

class MazeSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver")
        self.root.geometry("1000x500")
        self.root.configure(bg="#2E3440")
        self.maze = []
        self.create_widgets()

    def create_widgets(self):

        input_frame = tk.Frame(self.root, bg="#2E3440")
        input_frame.pack(side=tk.LEFT, padx=20, pady=20)


        self.label = tk.Label(input_frame, text="Enter Maze (10x10, use 'S' for start, 'E' for end, '#' for walls):",
                              bg="#2E3440", fg="#D8DEE9", font=("Helvetica", 12))
        self.label.pack(pady=10)


        self.entry = tk.Text(input_frame, height=10, width=40, bg="#3B4252", fg="#D8DEE9", insertbackground="#D8DEE9")
        self.entry.pack(pady=10)
        self.solve_button = tk.Button(input_frame, text="Solve Maze", command=self.solve_maze,
                                      bg="#4C566A", fg="#D8DEE9", font=("Helvetica", 12))
        self.solve_button.pack(pady=10)


        maze_frame = tk.Frame(self.root, bg="#2E3440")
        maze_frame.pack(side=tk.LEFT, padx=20, pady=20)
        self.original_canvas = tk.Canvas(maze_frame, width=400, height=400, bg="#3B4252", highlightthickness=0)
        self.original_canvas.grid(row=0, column=0, padx=10)


        self.solved_canvas = tk.Canvas(maze_frame, width=400, height=400, bg="#3B4252", highlightthickness=0)
        self.solved_canvas.grid(row=0, column=1, padx=10)

    def solve_maze(self):

        self.original_canvas.delete("all")
        self.solved_canvas.delete("all")


        maze_input = self.entry.get("1.0", tk.END).strip().split('\n')
        self.maze = [list(row) for row in maze_input]


        if len(self.maze) != 10 or any(len(row) != 10 for row in self.maze):
            self.label.config(text="Maze must be 10x10!")
            return


        start = None
        end = None
        for i in range(10):
            for j in range(10):
                if self.maze[i][j] == 'S':
                    start = (i, j)
                elif self.maze[i][j] == 'E':
                    end = (i, j)

        if not start or not end:
            self.label.config(text="Start or End not found!")
            return


        self.draw_maze(self.original_canvas, self.maze)


        path = self.bfs(start, end)
        if path:
            self.draw_maze(self.solved_canvas, self.maze, path)
            self.draw_path_direction(self.solved_canvas, path)
            self.label.config(text="Maze Solved!")
        else:
            self.label.config(text="No Solution Found!")

    def bfs(self, start, end):
        queue = deque([(start, [start])])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            (current, path) = queue.popleft()
            if current == end:
                return path

            for direction in directions:
                next_row, next_col = current[0] + direction[0], current[1] + direction[1]
                if 0 <= next_row < 10 and 0 <= next_col < 10 and self.maze[next_row][next_col] != '#':
                    self.maze[next_row][next_col] = '#'
                    queue.append(((next_row, next_col), path + [(next_row, next_col)]))

        return None

    def draw_maze(self, canvas, maze, path=None):
        cell_size = 40
        for i in range(10):
            for j in range(10):
                x0, y0 = j * cell_size, i * cell_size
                x1, y1 = x0 + cell_size, y0 + cell_size


                if maze[i][j] == '#':
                    canvas.create_rectangle(x0, y0, x1, y1, fill="#4C566A", outline="#4C566A")

                elif maze[i][j] == 'S':
                    canvas.create_rectangle(x0, y0, x1, y1, fill="#A3BE8C", outline="#4C566A")
                elif maze[i][j] == 'E':
                    canvas.create_rectangle(x0, y0, x1, y1, fill="#BF616A", outline="#4C566A")

                elif path and (i, j) in path:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="#88C0D0", outline="#4C566A")

                else:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="#3B4252", outline="#4C566A")

    def draw_path_direction(self, canvas, path):
        cell_size = 40
        for i in range(len(path) - 1):
            x1 = path[i][1] * cell_size + cell_size // 2
            y1 = path[i][0] * cell_size + cell_size // 2
            x2 = path[i + 1][1] * cell_size + cell_size // 2
            y2 = path[i + 1][0] * cell_size + cell_size // 2
            canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="#D8DEE9", width=3)

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeSolver(root)
    root.mainloop()