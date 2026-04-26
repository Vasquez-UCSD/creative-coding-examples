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

def draw_asset(model, rot_x, rot_y, scale_val, use_override):
    """Handles the 3D transformation and rendering"""
    if model:
        # Draw the Shape
        # model.enable_style()
        push_matrix()
        # Move to center of screen
        translate(width/2, height/2, 0)
        
        # Apply rotations
        rotate_x(rot_x)
        rotate_y(rot_y)
        
        # Apply the combined scale (Base Scale * Zoom Level)
        scale(scale_val / 100.0)
        
        shape(model)

        
        # Internal Override - Tells the engine to ingore the hardcoded material
        # and use the color/lights defined in the script (comment out if you prefer to use the model material)
        if use_override:
            model.disable_style()
            hint(DISABLE_DEPTH_TEST)
            
            no_fill()
            stroke(255)            
            stroke_weight(0.5)     
            shape(model)
            
            hint(ENABLE_DEPTH_TEST)
            model.enable_style()
        
        pop_matrix()
        
def get_poly_count(shape):
    if shape is None:
        return 0
    
    # Check if the shape is actually a group of shapes
    if shape.get_child_count() > 0:
        total = 0
        for i in range(shape.get_child_count()):
            # Recursively call this function for every child
            total += get_poly_count(shape.get_child(i))
        return total
    else:
        # It's a single shape, get the count using Py5 snake_case
        return shape.get_vertex_count() // 3