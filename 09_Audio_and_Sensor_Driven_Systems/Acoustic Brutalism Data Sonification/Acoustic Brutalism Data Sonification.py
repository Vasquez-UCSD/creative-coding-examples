analyzer = None
mic = None

def setup():
    size(800, 800)
    global analyzer, mic
    sound = get_library("processing.sound.*")
    mic = sound.AudioIn(this, 0)
    mic.start()
    analyzer = sound.Amplitude(this)
    analyzer.input(mic)
    stroke(255)
    no_fill()

def draw():
    global analyzer
    background(20, 50) # Slight transparency for motion blur
    
    volume = analyzer.analyze()
    
    # Move to center
    translate(width/2, height/2)
    
    # Create a 'brutalist' jagged shape based on volume
    begin_shape()
    for a in range(0, 361, 5):
        # The 'roughness' is driven by mic volume
        roughness = volume * 1000
        r = 200 + random(-roughness, roughness)
        
        x = cos(radians(a)) * r
        y = sin(radians(a)) * r
        vertex(x, y)
    end_shape(CLOSE)