import numpy as np
import glfw
import pyrr
from OpenGL.GL import *

from graphics import VBO, IBO, VAO, Shader

class App:
    def __init__(self, width, height):
        # Initialize glfw
        glfw.init()

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
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.5, 0.5, 0.0, 0.0, 0.0, 1.0,
            -0.5, 0.5, 0.0, 1.0, 0.0, 1.0
        ], dtype = np.float32)

        indices = np.array([
            0,1,2,
            0,3,2
        ], dtype = np.uint32)
        
        # Create VBO, IBO, VAO
        vbo = VBO(vertices)
        ibo = IBO(indices)
        vao = VAO(vbo)

        # Create shaders
        vertex_shader = '''
        
        #version 330 core
        layout(location = 0) in vec3 vertexPosition;
        layout(location = 1) in vec3 vertexColour;

        out vec3 fragmentColour;

        uniform mat4 modelMatrix;

        void main() {
            fragmentColour = vertexColour;
            // gl_Position = vec4(vertexPosition, 1.0);
            gl_Position = modelMatrix * vec4(vertexPosition, 1.0);
        }

        '''

        fragment_shader = '''

        #version 330 core

        in vec3 fragmentColour;

        out vec4 outputColour;

        void main() {
            outputColour = vec4(fragmentColour, 1.0); // Set color
        }

        '''

        shader = Shader(vertex_shader, fragment_shader)

        # Object position, rotation and scale
        position = np.array([0.0, 0.0, 0.0], dtype = np.float32)
        euler_rotation = np.array([0.0, 0.0, 0.0], dtype = np.float32)
        scale = np.array([1.0, 1.0, 1.0], dtype = np.float32)

        # Render loop
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            # Set background colour and clear previous frame
            glClearColor(0.2, 0.3, 0.3, 1.0) # RGBA
            glClear(GL_COLOR_BUFFER_BIT)

            # ----------
            # Make updates to the scene
            position[0] += 0.0001

            # Compute the uniforms
            translation_matrix = pyrr.matrix44.create_from_translation(position, dtype=np.float32).T
            scaling_matrix = pyrr.matrix44.create_from_scale(scale)
            rotation_matrix_x = pyrr.matrix44.create_from_x_rotation(np.radians(euler_rotation[0]), dtype=np.float32).T
            rotation_matrix_y = pyrr.matrix44.create_from_y_rotation(np.radians(euler_rotation[1]), dtype=np.float32).T
            rotation_matrix_z = pyrr.matrix44.create_from_z_rotation(np.radians(euler_rotation[2]), dtype=np.float32).T
            rotation_matrix = pyrr.matrix44.multiply(m1=rotation_matrix_z, m2=pyrr.matrix44.multiply(m1=rotation_matrix_y, m2=rotation_matrix_x))
            model_matrix =  pyrr.matrix44.multiply(m1=translation_matrix, m2=pyrr.matrix44.multiply(m1 = scaling_matrix, m2 = rotation_matrix))

            # Bind the shader, set uniforms, bind vao (automatically binds vbo) and ibo
            shader.Use()
            modelMatrixLocation = glGetUniformLocation(shader.ID, "modelMatrix".encode('utf-8'))
            glUniformMatrix4fv(modelMatrixLocation, 1, GL_TRUE, model_matrix)
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


