from drawer import Drawer
import OpenGL.GL as gl

from model_data import ModelData

class ColourDrawer(Drawer):

    def draw(self, data: ModelData):
        if data is None:
            raise TypeError('No model found in colour drawer.')
        
        if data.vertices is None:
            raise TypeError('No veritices found in colour drawer.')

        if data.colours is None:
            raise TypeError('No colours found in colour drawer.')
        
        if data.surfaces is None:
            raise TypeError('No surfaces found in colour drawer.')
        
        gl.glBegin(gl.GL_QUADS)
        for surface in data.surfaces:
            x = 0
            for vertex in surface:
                x+=1
                gl.glColor3fv(data.colours[x])
                gl.glVertex3fv(data.vertices[vertex])
        gl.glEnd()

        gl.glBegin(gl.GL_LINES)
        for edge in data.edges:
            for vertex in edge:
                gl.glVertex3fv(data.vertices[vertex])
        gl.glEnd()