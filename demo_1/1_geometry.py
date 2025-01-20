import numpy as np
import glfw
from OpenGL.GL import *

from graphics import VBO, IBO, VAO, Shader

class App:
    def __init__(self, width, height):
        # Initialize glfw
        glfw.init()
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        
        # Create a window using glfw
        self.windowHeight = height
        self.windowWidth = width
        self.window = glfw.create_window(width, height,"Demo", None, None)
        if not self.window:
            glfw.terminate()
            print("Glfw window can't be created")
            exit()

        # Set initial position on the screen and activate it
        glfw.set_window_pos(self.window, 500, 200) 
        glfw.make_context_current(self.window)

        # Set the viewport (Specifies which area to map the opengl co-ordinate system to)
        glViewport(0, 0, self.windowWidth, self.windowHeight)

    def RenderLoop(self):
        
        # Define Geometry
        vertices = np.array([
            -0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0, 0.5, 0.0
        ], dtype = np.float32)

        indices = np.array([
            0,1,2
        ], dtype = np.uint32)
        
        # Create VBO, IBO, VAO
        vbo = VBO(vertices)
        ibo = IBO(indices)
        vao = VAO(vbo)

        # Create shaders
        vertex_shader = '''
        
        #version 330 core
        layout(location = 0) in vec3 vertexPosition;
        void main() {
            gl_Position = vec4(vertexPosition, 1.0);
        }

        '''

        fragment_shader = '''

        #version 330 core
        out vec4 FragColor;
        void main() {
            FragColor = vec4(1.0, 1.0, 1.0, 1.0); // Set color
        }

        '''

        shader = Shader(vertex_shader, fragment_shader)

        # Render loop
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            # Set background colour and clear previous frame
            glClearColor(0.2, 0.3, 0.3, 1.0) # RGBA
            glClear(GL_COLOR_BUFFER_BIT)

            # ----------

            # Bind the shader, vao (automatically binds vbo) and ibo
            shader.Use()
            vao.Use()
            ibo.Use()

            # Issue Draw call with primitive type
            glDrawElements(GL_TRIANGLES, ibo.count, GL_UNSIGNED_INT, None)

            # ----------

            glfw.swap_buffers(self.window) 
        
        self.cleanUp()
    
    def cleanUp(self):
        # Shut down glfw window
        glfw.terminate()

if __name__ == "__main__":
    app = App(800, 600)
    app.RenderLoop()


