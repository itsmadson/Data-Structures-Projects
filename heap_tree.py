import tkinter as tk
from tkinter import ttk

class HeapTree:
    def __init__(self, root):
        self.root = root
        self.root.title("Heap Tree")
        self.root.geometry("800x600")
        self.root.configure(bg="#2E3440")
        self.heap = []
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#2E3440")
        style.configure("TLabel", background="#2E3440", foreground="#D8DEE9", font=("Helvetica", 12))
        style.configure("TButton", background="#4C566A", foreground="#D8DEE9", font=("Helvetica", 12), borderwidth=1)
        style.map("TButton", background=[("active", "#5E81AC")])

        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=20)

        self.label = ttk.Label(self.frame, text="Enter numbers to insert into the heap:")
        self.label.grid(row=0, column=0, pady=10)

        self.entry = tk.Entry(self.frame, width=40, bg="#3B4252", fg="#D8DEE9", insertbackground="#D8DEE9")
        self.entry.grid(row=1, column=0, pady=10)

        self.insert_button = ttk.Button(self.frame, text="Insert", command=self.insert)
        self.insert_button.grid(row=2, column=0, pady=10)

        self.delete_button = ttk.Button(self.frame, text="Delete Root", command=self.delete_root)
        self.delete_button.grid(row=3, column=0, pady=10)

        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="#3B4252", highlightthickness=0)
        self.canvas.pack()

    def insert(self):
        try:
            num = int(self.entry.get())
            self.heap.append(num)
            self.heapify_up(len(self.heap) - 1)
            self.draw_heap()
        except ValueError:
            self.label.config(text="Please enter a valid integer!")

    def delete_root(self):
        if len(self.heap) == 0:
            self.label.config(text="Heap is empty!")
            return
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.heapify_down(0)
        self.draw_heap()

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def draw_heap(self):
        self.canvas.delete("all")
        if not self.heap:
            return

        levels = self.calculate_levels()
        x = 400
        y = 50
        x_gap = 200

        for i in range(len(self.heap)):
            level = self.calculate_level(i)
            x_pos = x + (i - (2 ** level - 1)) * x_gap / (2 ** level)
            y_pos = y + level * 100
            self.canvas.create_oval(x_pos - 20, y_pos - 20, x_pos + 20, y_pos + 20, fill="#88C0D0", outline="#4C566A")
            self.canvas.create_text(x_pos, y_pos, text=str(self.heap[i]), fill="#2E3440")

            if i != 0:
                parent = (i - 1) // 2
                parent_level = self.calculate_level(parent)
                parent_x = x + (parent - (2 ** parent_level - 1)) * x_gap / (2 ** parent_level)
                parent_y = y + parent_level * 100
                self.canvas.create_line(parent_x, parent_y + 20, x_pos, y_pos - 20, fill="#D8DEE9")

    def calculate_levels(self):
        return (len(self.heap) + 1).bit_length() - 1

    def calculate_level(self, index):
        return (index + 1).bit_length() - 1

if __name__ == "__main__":
    root = tk.Tk()
    app = HeapTree(root)
    root.mainloop()