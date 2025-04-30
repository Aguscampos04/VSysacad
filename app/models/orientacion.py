from dataclasses import dataclass

@dataclass(repr=True, eq=True)
class Orientacion():
    nombre: str = ""