from dataclasses import dataclass

@dataclass
class Persona:
        nombre: str

### dataclass

@dataclass
class PersonaDto (Persona):
    edad: int
    cat: str

person = PersonaDto("Arturo",24, "Dev")

print(person)