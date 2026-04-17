# PY5 IMPORTED MODE CODE

def load_asset(file_path):
    """Loads an OBJ file and returns a Py5Shape object"""
    try:
        # load_shape is the py5 equivalent to loadShape()
        model = load_shape(file_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def draw_asset(model, rot_x, rot_y, scale_val):
    """Handles the 3D transformation and rendering"""
    if model:
        push_matrix()
        # Move to center of screen
        translate(width/2, height/2, 0)
        
        # Apply rotations
        rotate_x(rot_x)
        rotate_y(rot_y)
        
        # Apply scaling
        scale(scale_val)
        
        # Set a 'Brutalist' wireframe style for now
        stroke(255)
        no_fill()
        
        shape(model)
        pop_matrix()