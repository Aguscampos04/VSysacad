from dataclasses import dataclass
from cargo import Cargo

@dataclass(init=False, repr= True , eq=True)
class CategoriaCargo(Cargo):
        nombre: str