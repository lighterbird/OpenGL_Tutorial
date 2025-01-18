import ctypes
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class VBO:
    def __init__(self, vertices):
        self.ID = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.ID)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    def Use(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.ID)
    def Delete(self):
        glDeleteBuffers(1, (self.ID,))

class IBO:
    def __init__(self, indices):
        self.ID = glGenBuffers(1)
        self.count = len(indices)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ID)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)
    def Use(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ID)
    def Delete(self):
        glDeleteBuffers(1, (self.ID,))

class VAO:
    def __init__(self, vbo : VBO):
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        vbo.Use()
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, ctypes.c_uint(3 * ctypes.sizeof(ctypes.c_float)), ctypes.c_void_p(0))
    def Use(self):
        glBindVertexArray(self.vao)
    def Delete(self):
        glDeleteVertexArrays(1, (self.vao,))

class Shader:
    def __init__(self, vertex_shader, fragment_shader):
        self.ID = compileProgram(compileShader(vertex_shader, GL_VERTEX_SHADER), compileShader(fragment_shader, GL_FRAGMENT_SHADER))
        self.Use()
    def Use(self):
        glUseProgram(self.ID)
    def Delete(self):
        glDeleteProgram((self.ID,))