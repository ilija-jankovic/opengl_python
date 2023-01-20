from enum import Enum
from drawers.colour_drawer import ColourDrawer
from drawers.line_drawer import LineDrawer

from game_object import GameObject
from model import Model
from model_data import ModelData, ModelType

class Terrain(Enum):
    Void = ' '
    Block = '*'

def _create_block(x: float, y: float):
    data = ModelData.from_type(ModelType.Cube)
    model = Model(data)
    return GameObject(x=x, y=y, model=model, drawers=[LineDrawer(), ColourDrawer()])

def _create_player(x: float, y: float):
    data = ModelData.from_type(ModelType.Player)
    model = Model(data)
    return GameObject(x=x, y=y, model=model, drawers=[LineDrawer(), ColourDrawer()])

class Map:
    terrain: list[list[Terrain]]

    def decode(self, encoded: list[str]):
        terrain: list[list[Terrain]] = []

        for row in encoded:
            decoded_row = []
            terrain.append(decoded_row)
            for x in row:
                decoded_row.append(Terrain(x))
        
        return terrain
    
    def __init__(self, encoded: list[str]):
        self.terrain = self.decode(encoded)

    def create_game_objects(self, player_x: float, player_y: float):
        height = len(self.terrain)
        width = len(self.terrain[0])

        objs = [_create_block(x, -y) 
            for y in range(height) for x in range(width) 
            if self.terrain[y][x] is Terrain.Block]

        objs.append(_create_player(player_x, -player_y))

        return objs
        

