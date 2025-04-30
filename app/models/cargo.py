from dataclasses import dataclass

@dataclass(repr=True, eq=True)
class Cargo:
        nombre: str = ""
        puntos: str = ""
        