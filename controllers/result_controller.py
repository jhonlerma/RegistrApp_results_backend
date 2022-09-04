from models.result_model import ResultModel
from db.result_repository import ResultRepository

class ResultController():

    def __init__(self) -> None:
        self.repo = ResultRepository()

    def get_all(self, args):
        return list(self.repo.get_all())

    def get_by_id(self, id):
        pass

    def create(self, data):
        pass

    def update(self, id, data):
        pass

    def delete(self, id):
        pass
