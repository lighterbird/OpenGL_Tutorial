import numpy as np

obj1Verts = [
    #   x,   y,   z,    r,   g,   b
    -1, -1, -1,   1.0, 0.0, 0.0,  # Red
    -1, -1,  1,   0.0, 1.0, 0.0,  # Green
    -1,  1, -1,   0.0, 0.0, 1.0,  # Blue
    -1,  1,  1,   1.0, 1.0, 0.0,  # Yellow
     1, -1, -1,   1.0, 0.0, 1.0,  # Magenta
     1, -1,  1,   0.0, 1.0, 1.0,  # Cyan
     1,  1, -1,   1.0, 1.0, 1.0,  # White
     1,  1,  1,   0.0, 0.0, 0.0   # Black
]
obj1Inds = [
    0, 1, 3,  
    0, 3, 2,  
    4, 5, 7,  
    4, 7, 6,  
    0, 1, 5,  
    0, 5, 4,  
    2, 3, 7, 
    2, 7, 6,  
    0, 2, 6,  
    0, 6, 4,  
    1, 3, 7,  
    1, 7, 5   
]
obj1Props = {
    'vertices' : np.array(obj1Verts, dtype = np.float32),
    
    'indices' : np.array(obj1Inds, dtype = np.uint32),

    'position' : np.array([0, 0, 0], dtype = np.float32),

    'rotation' : np.array([0, 0, 0], dtype = np.float32),

    'scale' : np.array([1, 1, 1], dtype = np.float32),
}