from py5 import *
import config
from camera_engine import CameraEngine
from star_system import Star

cam = CameraEngine()
offscreen = None

def setup():
    global offscreen
    size(1200, 800, P3D) # P3D is required for texture mapping
    offscreen = create_graphics(1200, 800)
    config.stars = [Star(width, height) for i in range(config.star_count)]
    color_mode(HSB, 360, 100, 100)

def draw():
    background(0)
    
    # 1. Draw the Star System into the offscreen buffer
    offscreen.begin_draw()
    offscreen.background(0)
    offscreen.color_mode(HSB, 360, 100, 100)
    for s in config.stars:
        s.update()
        s.draw_to_buffer(offscreen)
    offscreen.end_draw()
    
    # 2. Draw the Keystoned Result to the main screen
    no_stroke()
    begin_shape()
    texture(offscreen)
    # Map corners: vertex(screen_x, screen_y, texture_u, texture_v)
    vertex(config.projection_corners[0][0], config.projection_corners[0][1], 0, 0)
    vertex(config.projection_corners[1][0], config.projection_corners[1][1], 1200, 0)
    vertex(config.projection_corners[2][0], config.projection_corners[2][1], 1200, 800)
    vertex(config.projection_corners[3][0], config.projection_corners[3][1], 0, 800)
    end_shape()
        
    draw_hud()
    draw_calibration_ui()

def draw_calibration_ui():
    # Draw draggable handles for the corners
    for i, p in enumerate(config.projection_corners):
        fill(0, 100, 100) # Bright red in HSB
        circle(p[0], p[1], 15)
        fill(255)
        text(str(i), p[0] + 10, p[1] - 10)

def draw_hud():
    # Capture Button
    hint(DISABLE_DEPTH_TEST) # Ensure HUD is on top
    fill(200, 100, 40, 200)
    stroke(255)
    rect(50, height - 100, 150, 50, 10)
    fill(255); text_align(CENTER, CENTER)
    text("CAPTURE MASK", 125, height - 75)
    
    if config.is_mask_active:
        text_align(LEFT)
        text("MASK ACTIVE (Press 'R' to Reset)", 220, height - 75)

def mouse_pressed():
    # Check if clicking button
    if 50 < mouse_x < 200 and height - 100 < mouse_y < height - 50:
        cam.capture_silhouette()
        return

    # Check if clicking a corner handle
    for i, p in enumerate(config.projection_corners):
        if dist(mouse_x, mouse_y, p[0], p[1]) < 20:
            config.corner_to_drag = i
            break

def mouse_dragged():
    if config.corner_to_drag != -1:
        config.projection_corners[config.corner_to_drag][0] = mouse_x
        config.projection_corners[config.corner_to_drag][1] = mouse_y

def mouse_released():
    config.corner_to_drag = -1

def key_pressed():
    if key.lower() == 'r':
        config.is_mask_active = False
        config.silhouette_mask = None

def exiting():
    cam.close()

if __name__ == '__main__':
    run_sketch()