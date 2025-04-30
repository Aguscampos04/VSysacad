from dataclasses import dataclass

@dataclass(repr=True, eq=True)
class Departamento:
        nombre: str = ""