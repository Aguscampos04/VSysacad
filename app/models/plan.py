from dataclasses import dataclass
from orientacion import Orientacion

@dataclass(init=False, repr= True , eq=True)
class Plan(Orientacion):
        nombre: str
        fechaInicio: str
        fechaFin: str
        observacion:str