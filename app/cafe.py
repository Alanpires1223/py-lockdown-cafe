import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Verifica se está vacinado
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitante não possui vacina registrada")

        # Verifica se a vacina está vencida
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vacina do visitante está vencida")

        # Verifica se está usando máscara
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitante não está usando máscara")

        return f"Welcome to {self.name}"
