from dataclasses import dataclass

@dataclass(init=False, repr= True , eq=True)
class Cargo:
    def __init__(self):
        nombre: str
        puntos: str
        