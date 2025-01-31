import numpy as np
import glfw
from OpenGL.GL import *

from graphics import VBO, IBO, VAO, Shader, Object, Camera
from assets.objects import obj1Props
from assets.shaders import objShaderSource

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
        glfw.set_window_pos(self.window, 450, 30) 
        glfw.make_context_current(self.window)

        # Enable depth testing
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS) 

        # Set the viewport (Specifies which area to map the opengl co-ordinate system to)
        glViewport(0, 0, self.windowWidth, self.windowHeight)

        # Delta time
        self.prevTime = glfw.get_time()

        # Initialize scene
        self.InitScene()

    def Close(self):
        glfw.terminate()
    
    def IsOpen(self):
        return not glfw.window_should_close(self.window)

    def StartFrame(self, c0, c1, c2, c3):
        currentTime = glfw.get_time()
        deltaTime = currentTime - self.prevTime
        self.prevTime = currentTime
        time = {"currentTime" : currentTime, "deltaTime" : deltaTime}

        glfw.poll_events()
        
        inputs = []
        if glfw.get_key(self.window, glfw.KEY_W) == glfw.PRESS:
            inputs.append("W")
        if glfw.get_key(self.window, glfw.KEY_A) == glfw.PRESS:
            inputs.append("A")
        if glfw.get_key(self.window, glfw.KEY_S) == glfw.PRESS:
            inputs.append("S")
        if glfw.get_key(self.window, glfw.KEY_D) == glfw.PRESS:
            inputs.append("D")
        if glfw.get_key(self.window, glfw.KEY_SPACE) == glfw.PRESS:
            inputs.append("SPACE")

        glClearColor(c0, c1, c2, c3)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        return inputs, time
    
    def EndFrame(self):
        glfw.swap_buffers(self.window) 

    def InitScene(self):
        self.camera = Camera(self.windowHeight, self.windowWidth)
        self.shaders = [Shader(objShaderSource["vertex_shader"], objShaderSource["fragment_shader"])]
        self.objects = [Object(self.shaders[0], obj1Props)]
    
    def ProcessFrame(self, inputs, time):
        # Update the object based on inputs
        self.objects[0].properties["velocity"] = np.array([0,0,0], dtype=np.float32)
        if "W" in inputs:
            self.objects[0].properties["velocity"][1] = self.objects[0].properties["sens"]
        if "S" in inputs:
            self.objects[0].properties["velocity"][1] = -self.objects[0].properties["sens"]
        if "A" in inputs:
            self.objects[0].properties["velocity"][0] = -self.objects[0].properties["sens"]
        if "D" in inputs:
            self.objects[0].properties["velocity"][0] = self.objects[0].properties["sens"]
        
        self.objects[0].properties["position"] += self.objects[0].properties["velocity"] * time["deltaTime"]

        # Update the camera matrix in shaders
        for shader in self.shaders:
            self.camera.Update(shader)

        # Draw the object
        for obj in self.objects:
            obj.Draw()

    def RenderLoop(self):
       
        while self.IsOpen():
            inputs, time = self.StartFrame(0.0, 0.0, 0.0, 1.0)
            self.ProcessFrame(inputs, time)
            self.EndFrame()
        
        self.Close()

if __name__ == "__main__":
    app = App(1000, 1000)
    app.RenderLoop()


