from .base import BaseCrud
from ..models import Character


class CharacterCrud(BaseCrud):

    def __init__(self):
        super().__init__(Character)
