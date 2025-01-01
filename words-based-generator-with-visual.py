import tkinter as tk
from super_duper import World

class WorldVisualizer:
    def __init__(self, world):
        self.world = world
        self.cell_size = (30 / 15) * 6
        
        self.root = tk.Tk()
        self.root.title("World Visualizer")
        
        self.canvas = tk.Canvas(
            self.root,
            width=self.world.width * self.cell_size,
            height=self.world.height * self.cell_size
        )
        self.canvas.pack()
        
        self.colors = {
            'G': 'green',
            'S': 'yellow',
            'W': 'blue',
            'B': 'red',
            'Y': 'purple',
            '_DEFAULT': 'white'
        }
        
        self.draw_world()
        
    def draw_world(self):
        for y in range(self.world.height):
            for x in range(self.world.width):
                x1 = x * self.cell_size
                y1 = y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                symbol = self.world.grid[y][x]['symbol']
                
                self.canvas.create_rectangle(
                    x1, y1,
                    x2, y2,
                    fill=self.colors.get(symbol, self.colors['_DEFAULT']),
                    outline='black'
                )
        
    def run(self):
        """Start the Tkinter main loop"""
        self.root.mainloop()

if __name__ == "__main__":
    print("Available map types:")
    print("1. Dry")
    print("2. Normal")
    print("3. Mini-islands")
    
    choice = input("Select map type (1-3): ")
    map_type = 'normal'
    
    if choice == '1':
        map_type = 'dry'
    elif choice == '2':
        map_type = 'normal'
    elif choice == '3':
        map_type = 'mini-islands'
    else:
        print("Invalid choice, defaulting to normal map")
    
    world = World(map_type=map_type)
    visualizer = WorldVisualizer(world)
    visualizer.run()
