from typing import Annotated
from projeto03.maisum import autoriza_voto


def autoriza_voto (voto):
    from datetime import date
    atual = date.today().year
    idade = atual - A