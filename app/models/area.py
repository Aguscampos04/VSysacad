from dataclasses import dataclass
 
@dataclass(init=False, repr= True , eq=True)
class Area:
    def __init__(self):
        nombre: str