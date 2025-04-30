from dataclasses import dataclass

@dataclass(repr=True, eq=True)
class Grado:
        nombre: str = ""