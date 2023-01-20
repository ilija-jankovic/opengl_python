from dataclasses import dataclass
from typing import Optional
from enum import Enum
import json
import copy

class ModelType(Enum):
    Cube = 'cube'
    Player = 'player'

@dataclass
class ModelData:
    vertices: Optional[list[list]] = None
    edges: Optional[list[list]] = None
    colours: Optional[list[list]] = None
    surfaces: Optional[list[list]] = None

    @staticmethod
    def from_type(type: ModelType):
        # TODO: Test performance hit.
        return copy.deepcopy(_cached_models[type])

def _cache(type: ModelType):
    f = open(f'models/{type.value}.json')
    data: dict = json.load(f)
    f.close()

    # Normalise length between -1 and 1 to 1.
    vertices = [[v[0]*0.5, v[1]*0.5, v[2]*0.5] for v in data.get('vertices')]

    edges = data.get('edges')
    colours = data.get('colours')
    surfaces = data.get('surfaces')

    return ModelData(vertices=vertices, edges=edges,
        colours=colours, surfaces=surfaces)

_cached_models: dict = {}
for type in ModelType:
    _cached_models[type] = _cache(type)
