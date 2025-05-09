from dataclasses import dataclass

@dataclass(repr=True, eq=True)
class Facultad:
    nombre: str = ""
    abreviatura: str = ""
    directorio: str = ""
    sigla: str = ""
    codigoPostal: str = ""
    ciudad: str = ""
    domicilio: str = ""
    telefono: str = ""
    contacto: str = ""
    email: str = ""
