# --- Global State ---
flowers = []
flower_color = color(255) # Default white
flower_count = 50
grid_size = 40

class Flower:
    def __init__(self, x, y):
        self.grid_x = x
        self.grid_y = y
        self.offset = random(TWO_PI) # Unique starting phase for the 'dance'

    def display(self, wx, wy, wz):
        push_matrix()
        # 1. Base position on terrain
        translate(wx, wy, wz)
        
        # 2. The "Dance" Logic
        # mouse_x controls speed, mouse_y controls intensity/sway
        sway_speed = remap(mouse_x, 0, width, 0.01, 0.2)
        sway_intensity = remap(mouse_y, 0, height, 0, 50)
        
        dance_x = sin(frame_count * sway_speed + self.offset) * sway_intensity
        dance_y = cos(frame_count * sway_speed + self.offset) * (sway_intensity * 0.5)
        
        # 3. Draw the Flower
        stroke(flower_color, 150)
        line(0, 0, 0, dance_x, dance_y, 40) # Stem
        
        translate(dance_x, dance_y, 40)
        no_stroke()
        fill(flower_color)
        sphere(8)
        pop_matrix()

def setup():
    size(1000, 800, P3D)
    # Initialize the first batch of flowers
    update_flower_population()

def draw():
    background(15)
    
    # Static Lighting
    ambient_light(50, 50, 50)
    point_light(255, 255, 255, 0, 0, 400)

    # View Controls
    translate(width/2, height/2 + 100, -200)
    rotate_x(radians(65))
    rotate_z(frame_count * 0.005) # Slow world rotation
    
    spacing = 40
    world_offset = (grid_size * spacing) / 2
    
    # Draw Terrain and Flowers
    no_fill()
    stroke(255, 30)
    for y in range(grid_size - 1):
        begin_shape(TRIANGLE_STRIP)
        for x in range(grid_size):
            # Same noise logic for terrain
            z = noise(x * 0.1, y * 0.1, frame_count * 0.01) * 150
            wx = x * spacing - world_offset
            wy = y * spacing - world_offset
            vertex(wx, wy, z)
            
            # Draw flowers belonging to this grid cell
            for f in flowers:
                if floor(f.grid_x) == x and floor(f.grid_y) == y:
                    f.display(wx, wy, z)
                    
            z2 = noise(x * 0.1, (y + 1) * 0.1, frame_count * 0.01) * 150
            vertex(wx, (y + 1) * spacing - world_offset, z2)
        end_shape()

# --- Input Handling ---

def key_pressed():
    global flower_count, flower_color
    
    # 1. Numbers (1-9) for Density
    if key.isdigit():
        val = int(key)
        if val == 0: val = 10
        flower_count = val * 50
        update_flower_population()
        print(f"Population set to: {flower_count}")

    # 2. Letters (A-Z) for Full Spectrum Color
    if key.isalpha():
        # Get the ASCII value (a=97, z=122)
        ascii_val = ord(key.lower())
        
        # REMAP the alphabet range (97-122) to the HSB range (0-360)
        hue_val = remap(ascii_val, 97, 122, 0, 360)
        
        # Set the color using HSB temporarily
        color_mode(HSB, 360, 100, 100)
        flower_color = color(hue_val, 85, 90)
        color_mode(RGB, 255) # Switch back to default RGB for other rendering
        
        print(f"Key: {key} | Hue: {int(hue_val)}°")

def update_flower_population():
    global flowers, flower_count
    flowers = []
    for _ in range(flower_count):
        flowers.append(Flower(random(grid_size), random(grid_size)))