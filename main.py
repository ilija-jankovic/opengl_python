# Modified example from: https://github.com/rougier/pyglfw/blob/master/simple.py
# and https://pypi.org/project/glfw/

import glfw
import OpenGL.GL as gl
import OpenGL.GLU as glu
from drawers.colour_drawer import ColourDrawer
from drawers.line_drawer import LineDrawer

from game_object import GameObject
from map import Map
from model import Model
from model_data import ModelType, ModelData

map = Map([
    '  *  ',
    '*****',
    '  *  ',
    '  *  ',
])

def on_pressed(window, key, scancode, action, mods):
    if action == glfw.PRESS:
        if key == glfw.KEY_RIGHT:
            gl.glTranslatef(-0.5, 0.0, 0.0)
            player.translate(0.5, 0.0, 0.0)
        elif key == glfw.KEY_LEFT:
            gl.glTranslatef(0.5, 0.0, 0.0)
            player.translate(-0.5, 0.0, 0.0)
        elif key == glfw.KEY_UP:
            gl.glTranslatef(0.0, -0.5, 0.0)
            player.translate(0.0, 0.5, 0.0)
        elif key == glfw.KEY_DOWN:
            gl.glTranslatef(0.0, 0.5, 0.0)
            player.translate(0.0, -0.5, 0.0)

def main():
    # Initialize the library
    if not glfw.init():
        return
    #print(glfw.vulkan_supported())
    # Create a windowed mode window and its OpenGL context
    width = 640
    height = 480
    window = glfw.create_window(width, height, 'Open GL Python', None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    ratio = width / float(height)
    glu.gluPerspective(45, (ratio), 0.1, 50.0)
    gl.glTranslatef(0.0,0.0, -5)

    glfw.set_key_callback(window, on_pressed)

    objs = map.create_game_objects(player_x=0, player_y=1);

    global player
    player = objs[len(objs)-1]

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here

        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

        for obj in objs:
            obj.draw()

        #gl.glRotatef(1, 3, 1, 1)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()