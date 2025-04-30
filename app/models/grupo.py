from dataclasses import dataclass

@dataclass(repr=True, eq=True)
class Grupo:
        nombre: str = ""