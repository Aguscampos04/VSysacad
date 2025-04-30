from dataclasses import dataclass
from facultad import Facultad

@dataclass(repr=True, eq=True)
class Universidad(Facultad):
        nombre: str = ""
        sigla:str = ""