from dataclasses import dataclass
from typing import Optional
from enum import Enum
import json
import copy

class ModelType(Enum):
    Cube = 'cube'

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

    vertices = data.get('vertices')
    edges = data.get('edges')
    colours = data.get('colours')
    surfaces = data.get('surfaces')

    return ModelData(vertices=vertices, edges=edges,
        colours=colours, surfaces=surfaces)

_cached_models: dict = {}
for type in ModelType:
    _cached_models[type] = _cache(type)
