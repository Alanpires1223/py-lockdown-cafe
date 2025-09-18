# Classe base para erros relacionados à vacina
class VaccineError(Exception):
    pass

# Erro quando o visitante não está vacinado
class NotVaccinatedError(VaccineError):
    def __init__(self, message="Visitante não está vacinado"):
        super().__init__(message)

# Erro quando a vacina do visitante está vencida
class OutdatedVaccineError(VaccineError):
    def __init__(self, message="Vacina do visitante está vencida"):
        super().__init__(message)

# Erro quando o visitante não está usando máscara
class NotWearingMaskError(Exception):
    def __init__(self, message="Visitante não está usando máscara"):
        super().__init__(message)
