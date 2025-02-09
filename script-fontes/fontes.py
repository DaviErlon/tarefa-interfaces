import tkinter as tk

class GridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("8x8 Grid Binary Converter")
        
        self.cell_size = 50
        self.grid_size = 8
        self.canvas_size = self.grid_size * self.cell_size
        
        # Matriz para armazenar o estado das células (0 ou 1)
        self.grid_state = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        
        # Configurar canvas
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.on_click)
        
        # Desenhar grade
        self.draw_grid()
        
        # Área de exibição dos valores
        self.info_frame = tk.Frame(root)
        self.info_frame.pack(pady=10)
        
        self.binary_labels = []
        self.hex_labels = []
        
        # Criar labels para cada linha
        for i in range(self.grid_size):
            binary_label = tk.Label(self.info_frame, text="00000000", width=10, anchor='w')
            hex_label = tk.Label(self.info_frame, text="0x00", width=5, anchor='w')
            
            binary_label.grid(row=i, column=0, padx=5)
            hex_label.grid(row=i, column=1, padx=5)
            
            self.binary_labels.append(binary_label)
            self.hex_labels.append(hex_label)
        
        # Atualizar exibição inicial
        self.update_display()

    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                
                self.canvas.create_rectangle(
                    x0, y0, x1, y1,
                    outline="black",
                    fill="white",
                    tags=(f"cell_{i}_{j}", "cell")
                )

    def on_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        
        if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
            self.toggle_cell(row, col)
            self.update_display()

    def toggle_cell(self, row, col):
        current_state = self.grid_state[row][col]
        new_state = 0 if current_state else 1
        self.grid_state[row][col] = new_state
        
        color = "black" if new_state else "white"
        self.canvas.itemconfig(f"cell_{row}_{col}", fill=color)

    def update_display(self):
        for i, row in enumerate(self.grid_state):
            # Converter para string binária
            binary_str = ''.join(str(bit) for bit in row)
            self.binary_labels[i].config(text=binary_str)
            
            # Converter para hexadecimal
            decimal_value = int(binary_str, 2)
            hex_str = f"0x{decimal_value:02X}"
            self.hex_labels[i].config(text=hex_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = GridApp(root)
    root.mainloop()