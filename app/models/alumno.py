from dataclasses import dataclass
 
@dataclass(init=False, repr= True , eq=True)
class Alumno:
    def __init__(self):
        nombre: str
        apellido: str
        nrodocumento: str
        tipodocumento: str
        fechanacimiento: str
        sexo: str
        nrolegajo: int
        fechaingreso: str