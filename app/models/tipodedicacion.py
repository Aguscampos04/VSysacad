from dataclasses import dataclass
from cargo import Cargo

@dataclass(init=False, repr= True , eq=True)
class TipoDedicacion(Cargo):
    def __init__(self):
        nombre: str
        observacion: str