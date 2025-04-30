from dataclasses import dataclass
from orientacion import Orientacion

@dataclass(repr=True, eq=True)
class Materia(Orientacion):
    nombre: str = ""
    codigo: str = ""
    observacion: str = ""