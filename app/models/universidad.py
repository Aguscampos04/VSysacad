from dataclasses import dataclass
from facultad import Facultad

@dataclass(init=False, repr= True , eq=True)
class Universidad(Facultad):
    def __init__(self):
        nombre: str
        sigla:str