# --- Global State ---
flowers = []
flower_color = None  # Initialized in setup()
flower_count = 100   # Default starting density
grid_size = 40       # Resolution of the terrain

class Flower:
    def __init__(self, x, y):
        self.grid_x = x
        self.grid_y = y
        self.offset = random(TWO_PI) # Unique starting phase for the sway

    def display(self, wx, wy, wz):
        pushMatrix()
        # 1. Position on terrain height (wz)
        translate(wx, wy, wz)
        
        # 2. The "Dance" Logic
        # mouseX controls speed, mouseY controls sway intensity
        sway_speed = map(mouseX, 0, width, 0.01, 0.2)
        sway_intensity = map(mouseY, 0, height, 0, 50)
        
        dance_x = sin(frameCount * sway_speed + self.offset) * sway_intensity
        dance_y = cos(frameCount * sway_speed + self.offset) * (sway_intensity * 0.5)
        
        # 3. Draw the Flower
        # Note: In P3D, -Z is 'up' after our X-axis rotation
        stroke(flower_color, 180)
        strokeWeight(2)
        line(0, 0, 0, dance_x, dance_y, 40) # Stem growing UP
        
        translate(dance_x, dance_y, 40) # Move to top of stem
        noStroke()
        fill(flower_color)
        sphere(8) # Flower head
        popMatrix()

def setup():
    size(1000, 800, P3D)
    global flower_color
    flower_color = color(200, 100, 255) # Starting Purple
    update_flower_population()

def draw():
    background(15)
    
    # Lighting
    ambientLight(60, 60, 60)
    pointLight(255, 255, 255, 0, 0, 500)

    # View Controls
    translate(width/2, height/2 + 100, -200)
    rotateX(radians(65))           # Tilts the world to see depth
    rotateZ(frameCount * 0.005)    # Slow world rotation
    
    spacing = 40
    world_offset = (grid_size * spacing) / 2
    
    # --- Part 1: Draw Terrain ---
    noFill()
    stroke(255, 40)
    strokeWeight(1)
    for y in range(grid_size - 1):
        beginShape(TRIANGLE_STRIP)
        for x in range(grid_size):
            # Noise-based terrain height
            z1 = noise(x * 0.1, y * 0.1, frameCount * 0.01) * 150
            wx = x * spacing - world_offset
            wy = y * spacing - world_offset
            vertex(wx, wy, z1)
            
            z2 = noise(x * 0.1, (y + 1) * 0.1, frameCount * 0.01) * 150
            vertex(wx, (y + 1) * spacing - world_offset, z2)
        endShape()

    # --- Part 2: Draw Flowers ---
    for f in flowers:
        # Snap flower to its grid coordinates
        fx = int(f.grid_x)
        fy = int(f.grid_y)
        
        # Calculate matching Z height from noise
        fz = noise(fx * 0.1, fy * 0.1, frameCount * 0.01) * 150
        fwx = fx * spacing - world_offset
        fwy = fy * spacing - world_offset
        
        f.display(fwx, fwy, fz)

# --- Input Handling ---

def keyPressed():
    global flower_count, flower_color
    
    # 1. Numbers (1-9) change population density
    if str(key).isdigit():
        val = int(str(key))
        if val == 0: val = 10
        flower_count = val * 30
        update_flower_population()
        print("Population: " + str(flower_count))

    # 2. Letters (A-Z) change flower color via HSB mapping
    if str(key).isalpha():
        ascii_val = ord(str(key).lower())
        hue_val = map(ascii_val, 97, 122, 0, 360)
        
        colorMode(HSB, 360, 100, 100)
        flower_color = color(hue_val, 80, 90)
        colorMode(RGB, 255) # Return to RGB for rest of scene
        
        print("Hue set to: " + str(int(hue_val)))

def update_flower_population():
    global flowers, flower_count
    flowers = []
    for _ in range(flower_count):
        # Place flowers randomly within the grid bounds
        flowers.append(Flower(random(grid_size-1), random(grid_size-1)))
