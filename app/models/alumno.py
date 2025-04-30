from dataclasses import dataclass

@dataclass(repr=True, eq=True)
class Alumno:
    nombre: str = ""
    apellido: str = ""
    nrodocumento: str = ""
    tipodocumento: str = ""
    fechanacimiento: str = ""
    sexo: str = ""
    nrolegajo: int = 0
    fechaingreso: str = ""
