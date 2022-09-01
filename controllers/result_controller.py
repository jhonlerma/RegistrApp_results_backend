from models.result_model import ResultModel
from db.result_repository import ResultRepository


class ResultController():

    def __init__(self) -> None:
        self.repo = ResultRepository()

    def get_all(self, args):
        return list(self.repo.get_all())

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data):
        result = ResultModel(data)
        # todo or do never XD validate fields
        return {
            "id": self.repo.save(result)
        }

    def update(self, id, data):
        result = ResultModel(data)
        self.repo.update(id, result)


    def delete(self, id):
        self.repo.delete(id)
