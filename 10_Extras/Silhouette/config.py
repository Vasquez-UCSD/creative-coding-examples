import numpy as np

# Global States
is_mask_active = False 
silhouette_mask = None 
star_count = 2000 # Increased for a denser "fill"
stars = []

# Keystone Settings
# Default corners to the edges of the 1200x800 window
projection_corners = [[0, 0], [1200, 0], [1200, 800], [0, 800]]
corner_to_drag = -1