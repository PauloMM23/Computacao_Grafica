# A partir do Ex1 (Renderização de um triângulo.py) e Ex2 (renderização de um quadrado.py) 
# criar um novo código para gerar dois objetos na tela sobrepostos, ou seja, um em cima do outro: um quadrado com um triângulo em  cima. 

# Dica: Criar uma função para gerar o quadrado e outra para gerar o triangulo e usar as mesmas posições dos pontos e cores diferentes para poder diferenciar um do outro. 
# Basicamente o resto das configurações do OpenGL são os mesmos para os dois e devem ser configuradas nas duas funções, 
# junto com os valores dos pontos e das cores. Deverá ser postado o código fonte do algoritmo no formato *.py.

import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

Window = None
Shader_programm = None
Vao = None
WIDTH = 800
HEIGHT = 600

def redimensionaCallback(window, w, h):
    global WIDTH, HEIGHT
    WIDTH = w
    HEIGHT = h

def inicializaOpenGL():
    global Window, WIDTH, HEIGHT

    #Inicializa GLFW
    glfw.init()

    #Criação de uma janela
    Window = glfw.create_window(WIDTH, HEIGHT, "Exercício - renderização de um quadrado e um triângulo", None, None)
    if not Window:
        glfw.terminate()
        exit()

    glfw.set_window_size_callback(Window, redimensionaCallback)
    glfw.make_context_current(Window)

    print("Placa de vídeo: ",OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER))
    print("Versão do OpenGL: ",OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION))
    

def inicializaShaders():
    global Shader_programm
    # Especificação do Vertex Shader:
    vertex_shader = """
        #version 400
        layout(location = 0) in vec3 vertex_posicao;
        layout(location = 1) in vec3 vertex_cores;
        out vec3 cores;
        void main () {
            cores = vertex_cores;
            gl_Position = vec4 (vertex_posicao, 1.0);
        }
    """
    vs = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(vs, 512, None)
        print("Erro no vertex shader:\n", infoLog)

    # Especificação do Fragment Shader:
    fragment_shader = """
        #version 400
        in vec3 cores;
		out vec4 frag_colour;
		void main () {
		    frag_colour = vec4 (cores, 1.0);
		}
    """
    fs = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(fs, 512, None)
        print("Erro no fragment shader:\n", infoLog)

    # Especificação do Shader Programm:
    Shader_programm = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programm, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programm, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def inicializaRenderizacao(): # renderização do quadrado e do triângulo
    global Window, Shader_programm, Vao_quadrado, Vao_triangulo, WIDTH, HEIGHT

    while not glfw.window_should_close(Window):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glViewport(0, 0, WIDTH, HEIGHT)

        glUseProgram(Shader_programm)

        glBindVertexArray(Vao_quadrado)

        glDrawArrays(GL_TRIANGLES, 0, 6)

        glBindVertexArray(Vao_triangulo)

        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.poll_events()

        glfw.swap_buffers(Window)
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)):
            glfw.set_window_should_close(Window, True)
    
    glfw.terminate()

def inicializaQuadrado(): #modelagem do quadrado
    global Vao_quadrado
    # Vao do quadrado
    Vao_quadrado = glGenVertexArrays(1)
    glBindVertexArray(Vao_quadrado)

    # VBO dos vértices do quadrado
    points = [
        # triângulo 1
		0.5, 0.5, 0.0, #vertice superior direito
		0.5, -0.5, 0.0, #vertice inferior direito
		-0.5, -0.5, 0.0, #vertice inferior esquerdo
		#triângulo 2
		-0.5, 0.5, 0.0, #vertice superior esquerdo
		0.5, 0.5, 0.0, #vertice superior direito
		-0.5, -0.5, 0.0 #vertice inferior esquerdo
	]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		#triângulo 1
		1.0, 1.0, 0.0,#amarelo
		0.0, 1.0, 1.0,#ciano
		1.0, 0.0, 1.0,#magenta
		#triângulo 2
		0.0, 1.0, 1.0,#ciano
		1.0, 1.0, 0.0,#amarelo
		1.0, 0.0, 1.0,#magenta
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaTriangulo(): #modelagem do triângulo
    global Vao_triangulo
    Vao_triangulo = glGenVertexArrays(1)
    glBindVertexArray(Vao_triangulo)

    points = [
        #X    Y    Z
		0.0, 0.5, 0.0, #cima
		0.5, -0.5, 0.0, #direita
		-0.5, -0.5, 0.0 #esquerda
	]

    points = np.array(points, dtype=np.float32)

    pvbo = glGenBuffers(1) 
    glBindBuffer(GL_ARRAY_BUFFER, pvbo) 
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    cores = [
        #R    G    B
		1.0, 0.0, 0.0, #vermelho
		0.0, 1.0, 0.0, #verde
		0.0, 0.0, 1.0  #azul
	]
    cores = np.array(cores, dtype=np.float32) #converte o array para numpy
    cvbo = glGenBuffers(1) #gera o vbo para as cores
    glBindBuffer(GL_ARRAY_BUFFER, cvbo) #da um bind no vbo das cores
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW) #copia os dados para a memória de vídeo
    glEnableVertexAttribArray(1) #ativa o índice 1 para o vbo das cores
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None) #configura o vbo das cores

# Função principal
def main():
    inicializaOpenGL()
    inicializaQuadrado() #modelagem do quadrado
    inicializaTriangulo() #modelagem do triângulo
    inicializaShaders()
    inicializaRenderizacao()

if __name__ == "__main__":
    main()