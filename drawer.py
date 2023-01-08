from abc import ABC, abstractmethod

from model_data import ModelData

class Drawer(ABC):
    @abstractmethod
    def draw(self, data: ModelData):
        pass