from dataclasses import dataclass
from orientacion import Orientacion

@dataclass(init=False, repr= True , eq=True)
class Especialidad(Orientacion):
    def __init__(self):
        nombre: str
        letra: str
        observacion: str