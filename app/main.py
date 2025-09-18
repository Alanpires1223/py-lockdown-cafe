from app.cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "Todos os amigos devem estar vacinados"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Amigos devem comprar {masks_to_buy} máscaras"

    return f"Amigos podem ir ao {cafe.name}"
