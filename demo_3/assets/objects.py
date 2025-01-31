import numpy as np

def CreateCircle(center, radius, colour, points = 10):
    vertices = [center[0], center[1], center[2], colour[0], colour[1], colour[2]]
    indices = []

    for i in range(points):
        vertices += [
            center[0] + radius * np.cos(float(i * 2* np.pi)/points),
            center[1] + radius * np.sin(float(i * 2* np.pi)/points),
            center[2],
            colour[0],
            colour[1],
            colour[2],
            ]
        
        ind1 = i+1
        ind2 = i+2 if i != points-1 else 1
        indices += [0, ind1, ind2]

    return (vertices, indices)    

obj1Verts, obj1Inds = CreateCircle([0,0,0],1, [1,1,1], 20)
obj1Props = {
    'vertices' : np.array(obj1Verts, dtype = np.float32),
    
    'indices' : np.array(obj1Inds, dtype = np.uint32),

    'position' : np.array([0, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, 0, 0], dtype = np.float32)
}