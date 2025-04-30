from dataclasses import dataclass

@dataclass(repr=True, eq=True)
class Area:
        nombre: str = ""