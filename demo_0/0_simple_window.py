import glfw
from OpenGL.GL import *

# Initialize glfw
glfw.init()

# Create a window using glfw
height = 600
width = 800
window = glfw.create_window(width, height,"Demo", None, None)
if not window:
    glfw.terminate()
    print("Glfw window can't be created")
    exit()

# Set initial position on the screen and activate it
glfw.set_window_pos(window, 500, 200) 
glfw.make_context_current(window)

# Set the viewport (Specifies which area to map the opengl co-ordinate system to)
glViewport(0, 0, width, height)

# Render loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    # Set background colour and clear previous frame
    glClearColor(0.2, 0.3, 0.3, 1.0) # RGBA
    glClear(GL_COLOR_BUFFER_BIT)

    # ----------
    # Render here
    # ----------

    glfw.swap_buffers(window) 

# Shut down glfw window
glfw.terminate()