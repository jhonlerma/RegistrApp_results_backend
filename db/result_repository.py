from db.repository import Repository
from models.result_model import ResultModel


class ResultRepository(Repository[ResultModel]):
    def __init__(self):
        super().__init__()
