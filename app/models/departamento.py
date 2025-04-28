from dataclasses import dataclass
 
@dataclass(init=False, repr= True , eq=True)
class Departamento:
    def __init__(self):
        nombre: str