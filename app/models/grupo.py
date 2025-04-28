from dataclasses import dataclass
 
@dataclass(init=False, repr= True , eq=True)
class Grupo:
    def __init__(self):
        nombre: str