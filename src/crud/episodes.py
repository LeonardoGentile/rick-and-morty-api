from .base import BaseCrud
from ..models import Episode


class EpisodeCrud(BaseCrud):
    def __init__(self):
        super().__init__(Episode)
