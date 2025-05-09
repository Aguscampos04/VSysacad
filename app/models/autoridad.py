from dataclasses import dataclass
from facultad import Facultad

@dataclass(repr=True, eq=True)
class Autoridad(Facultad):
        nombre: str = ""
        cargo: str = ""
        telefono: str = ""
        email: str = ""