from drawer import Drawer
import OpenGL.GL as gl

from model_data import ModelData

class LineDrawer(Drawer):

    def draw(self, data: ModelData):
        if data is None:
            raise TypeError('No model found in line drawer.')
        
        if data.vertices is None:
            raise TypeError('No veritices found in line drawer.')

        if data.edges is None:
            raise TypeError('No lines found in line drawer.')
        
        gl.glBegin(gl.GL_LINES)
        for edge in data.edges:
            for vertex in edge:
                gl.glVertex3fv(data.vertices[vertex])
        gl.glEnd()