from dataclasses import dataclass
from cargo import Cargo

@dataclass(init=False, repr= True , eq=True)
class TipoDedicacion(Cargo):
        nombre: str
        observacion: str