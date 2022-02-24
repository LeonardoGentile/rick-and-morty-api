from src.crud.base import BaseCrud
from src.models import Comment


class CommentCrud(BaseCrud):

    def __init__(self):
        super().__init__(Comment)
