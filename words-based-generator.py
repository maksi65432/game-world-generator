import random

class World:
    def __init__(self, width=120, height=60, map_type='normal'):
        self.width = width
        self.height = height
        self.map_type = map_type
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.terrain_types = {
            'grass': {'symbol': 'G', 'blocking': False},
            'stone': {'symbol': 'S', 'blocking': True},
            'water': {'symbol': 'W', 'blocking': True},
            'sand': {'symbol': 'Y', 'blocking': False},
            'border': {'symbol': 'B', 'blocking': True}
        }
        self.generate_world()

    def generate_world(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    self.grid[y][x] = self.terrain_types['border']
                    continue

        inner_width = self.width - 2
        inner_height = self.height - 2
        total_inner_cells = inner_width * inner_height
        positions = [(x, y) for y in range(1, self.height-1) for x in range(1, self.width-1)]
        random.shuffle(positions)

        if self.map_type == 'dry':
            min_grass = int(total_inner_cells * 0.4)
            min_sand = int(total_inner_cells * 0.3)
            
            for x, y in positions[:min_grass]:
                self.grid[y][x] = self.terrain_types['grass']
            
            for x, y in positions[min_grass:min_grass + min_sand]:
                self.grid[y][x] = self.terrain_types['sand']
            
            for x, y in positions[min_grass + min_sand:]:
                terrain = random.choices(
                    ['stone', 'water'],
                    weights=[90, 10]
                )[0]
                self.grid[y][x] = self.terrain_types[terrain]

        elif self.map_type == 'mini-islands':
            num_islands = random.randint(20, 30)
            island_size = random.randint(3, 8)
            
            for _ in range(num_islands):
                center_x = random.randint(1, self.width-2)
                center_y = random.randint(1, self.height-2)
                
                for dx in range(-island_size, island_size+1):
                    for dy in range(-island_size, island_size+1):
                        x = center_x + dx
                        y = center_y + dy
                        if 1 <= x < self.width-1 and 1 <= y < self.height-1:
                            if random.random() < 0.7:
                                self.grid[y][x] = random.choice([
                                    self.terrain_types['grass'],
                                    self.terrain_types['sand']
                                ])
            
            for y in range(1, self.height-1):
                for x in range(1, self.width-1):
                    if self.grid[y][x] is None:
                        self.grid[y][x] = self.terrain_types['water']

        else:
            min_grass = int(total_inner_cells * 0.6)
            
            for x, y in positions[:min_grass]:
                self.grid[y][x] = self.terrain_types['grass']
            
            for x, y in positions[min_grass:]:
                terrain = random.choices(
                    ['stone', 'water'],
                    weights=[70, 30]
                )[0]
                self.grid[y][x] = self.terrain_types[terrain]

    def is_blocked(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]['blocking']
        return True

    def display(self):
        for row in self.grid:
            print(' '.join(cell['symbol'] for cell in row))

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
    print(f"\nGenerated {map_type} world:")
    world.display()
