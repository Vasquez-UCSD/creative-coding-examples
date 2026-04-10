# Import the Processing Sound library
add_library('sound')

volume = 0
amp = None

def setup():
    size(800, 800)
    background(20)
    global amp
    
    # Initialize the audio input (microphone)
    mic = AudioIn(this, 0)
    mic.start()
    
    # Create an Amplitude analyzer to track volume
    amp = Amplitude(this)
    amp.input(mic)

def draw():
    global volume
    
    # 1. MASKING THE BACKGROUND (Motion Blur)
    # Processing uses noStroke() and fill()
    noStroke()
    fill(20, 40) 
    rect(0, 0, width, height)
    
    # Get current volume (returns a value between 0.0 and 1.0)
    volume = amp.analyze()
    
    # 2. POSITIONING
    translate(width/2, height/2)
    
    # 3. DRAW BRUTALIST SHAPE
    stroke(255)
    strokeWeight(2) # Changed from stroke_weight
    noFill() # Changed from no_fill
    
    # Multiplier adjusted for the 0.0 - 1.0 range of amp.analyze()
    roughness = volume * 1200 
    
    beginShape() # Changed from begin_shape
    for a in range(0, 361, 5):
        # Base radius + random jitter driven by mic
        r = 200 + random(-roughness, roughness)
        
        # Convert polar to cartesian coordinates
        # Processing uses radians(), cos(), and sin() natively
        x = cos(radians(a)) * r
        y = sin(radians(a)) * r
        vertex(x, y)
    endShape(CLOSE) # Changed from end_shape

    # 4. HUD
    resetMatrix() # Changed from reset_matrix
    fill(255)
    textSize(14) # Changed from text_size
    
    # Using .format() for Jython compatibility instead of f-strings
    text("Mic Activity (RMS): {}".format(round(volume, 4)), 20, 30)
