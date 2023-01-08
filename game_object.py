from drawer import Drawer

from model import Model

class GameObject:
    def initialise(self, x: float, y: float, z: float):
        if self.model is not None:
            self.model.translate(x, y, z)

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0,
        model: Model = None, drawers: list[Drawer] = None):
        self.x: float = x
        self.y: float = y
        self.z: float = z
        self.model: Model = model
        self.drawers: list[Drawer] = drawers
        self.initialise(x, y, z)

    def draw(self):
        if self.drawers is not None:
            for drawer in self.drawers:
                drawer.draw(self.model.data)