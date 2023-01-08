from model_data import ModelData

class Model:
    def __init__(self, data: ModelData):
        self.data = data

    def translate(self, x: float, y: float, z: float):
        for v in self.data.vertices:
            v[0] += x
            v[1] += y
            v[2] += z