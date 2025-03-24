import tkinter as tk

class OSIVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("OSI Model Visualizer")
        self.root.geometry("1200x800")
        
        # Configuration
        self.layer_colors = {
            7: "#FFEBEE",  # Application
            6: "#F3E5F5",  # Presentation
            5: "#E8EAF6",  # Session
            4: "#E3F2FD",  # Transport
            3: "#E0F2F1",  # Network
            2: "#F1F8E9",  # Data Link
            1: "#FFF8E1"   # Physical
        }
        
        self.header_colors = {
            7: "#EF5350",
            6: "#AB47BC",
            5: "#5C6BC0",
            4: "#42A5F5",
            3: "#26A69A",
            2: "#9CCC65",
            1: "#FFCA28"
        }
        
        # Animation control
        self.animation_running = False
        self.current_headers = []
        
        # Create UI
        self.create_widgets()
        self.draw_osi_model()
    
    def create_widgets(self):
        # Create main container
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Control panel at top
        control_frame = tk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=10)
        
        # Start button
        self.btn = tk.Button(control_frame, 
                           text="Start Transmission",
                           command=self.toggle_animation,
                           font=("Arial", 12),
                           bg="#4CAF50",
                           fg="white")
        self.btn.pack(side=tk.LEFT, padx=20)
        
        # Status label
        self.status = tk.Label(control_frame, 
                             text="Click Start to begin",
                             font=("Arial", 10))
        self.status.pack(side=tk.LEFT)
        
        # Main canvas
        self.canvas = tk.Canvas(main_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def draw_osi_model(self):
        # Draw layers
        layer_height = 80
        for layer in range(7, 0, -1):
            y = 50 + (7 - layer) * layer_height
            # Sender side
            self.canvas.create_rectangle(50, y, 300, y + 60,
                                      fill=self.layer_colors[layer],
                                      outline="black")
            self.canvas.create_text(175, y + 30,
                                 text=f"Layer {layer}\n{self.layer_name(layer)}",
                                 justify="center")
            
            # Receiver side
            self.canvas.create_rectangle(900, y, 1150, y + 60,
                                      fill=self.layer_colors[layer],
                                      outline="black")
            self.canvas.create_text(1025, y + 30,
                                 text=f"Layer {layer}\n{self.layer_name(layer)}",
                                 justify="center")
        
        # Transmission medium
        self.canvas.create_line(300, 600, 900, 600, width=3,
                              arrow=tk.BOTH, dash=(5, 2))
        self.canvas.create_text(600, 590, text="Physical Transmission",
                             font=("Arial", 12, "bold"))

    def layer_name(self, layer):
        names = {
            7: "Application",
            6: "Presentation",
            5: "Session",
            4: "Transport",
            3: "Network",
            2: "Data Link",
            1: "Physical"
        }
        return names[layer]

    def create_packet(self, x, y):
        # Create packet with headers
        packet = self.canvas.create_rectangle(x, y, x + 200, y + 40,
                                            fill="#4CAF50", outline="black")
        text_x = x + 10
        for layer in self.current_headers:
            self.canvas.create_rectangle(text_x - 5, y + 5, text_x + 30, y + 35,
                                       fill=self.header_colors[layer])
            self.canvas.create_text(text_x + 12, y + 20, text=f"L{layer}",
                                  fill="white")
            text_x += 40
        self.canvas.create_text(text_x + 10, y + 20, text="Data", anchor="w")
        return packet

    def animate_encapsulation(self, layer=7):
        if layer < 1:
            self.animate_transmission()
            return
            
        y = 85 + (7 - layer) * 80
        self.current_headers.append(layer)
        self.canvas.delete("packet")
        self.create_packet(100, y)
        self.update_status(f"Encapsulating Layer {layer}")
        self.root.after(800, lambda: self.animate_encapsulation(layer - 1))

    def animate_transmission(self):
        self.canvas.delete("packet")
        packet = self.create_packet(300, 570)
        self.move_packet(packet, 300, 570, 900, 570)

    def move_packet(self, packet, x1, y1, x2, y2):
        if x1 < x2:
            self.canvas.move(packet, 5, 0)
            self.root.after(20, lambda: self.move_packet(packet, x1+5, y1, x2, y2))
        else:
            self.animate_decapsulation()

    def animate_decapsulation(self, layer=1):
        if layer > 7:
            self.complete_animation()
            return
            
        y = 85 + (7 - layer) * 80
        if self.current_headers:
            self.current_headers.pop()
            
        self.canvas.delete("packet")
        self.create_packet(900, y)
        self.update_status(f"Decapsulating Layer {layer}")
        self.root.after(800, lambda: self.animate_decapsulation(layer + 1))

    def update_status(self, message):
        self.status.config(text=message)
        self.root.update()

    def complete_animation(self):
        self.animation_running = False
        self.btn.config(text="Start Transmission", bg="#4CAF50")
        self.status.config(text="Transmission Complete!")
        self.canvas.delete("packet")

    def toggle_animation(self):
        if not self.animation_running:
            self.animation_running = True
            self.btn.config(text="Cancel Transmission", bg="#F44336")
            self.current_headers = []
            self.canvas.delete("packet")
            self.animate_encapsulation()
        else:
            self.animation_running = False
            self.complete_animation()

if __name__ == "__main__":
    root = tk.Tk()
    app = OSIVisualizer(root)
    root.mainloop()
