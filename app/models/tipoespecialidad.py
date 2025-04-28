from dataclasses import dataclass
from especialidad import Especialidad

@dataclass(init=False, repr= True , eq=True)
class TipoEspecialidad(Especialidad):
    nombre: str
    nivel: str