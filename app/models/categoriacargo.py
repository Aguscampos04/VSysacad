from dataclasses import dataclass
from cargo import Cargo

@dataclass(repr=True, eq=True)
class CategoriaCargo(Cargo):
        nombre: str = ""