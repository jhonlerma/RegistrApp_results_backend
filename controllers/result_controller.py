from models.result_model import ResultModel
from models.table_model import TableModel
from models.candidate_model import CandidateModel
from db.result_repository import ResultRepository
from db.table_repository import TableRepository
from db.candidate_repository import CandidateRepository


class ResultController():

    def __init__(self) -> None:
        self.repo = ResultRepository()
        self.table_repo = TableRepository()
        self.candidate_repo = CandidateRepository()

    def get_all(self, args):
        return list(self.repo.get_all())

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data, table_id, candidate_id):
        result = ResultModel(data)
        table = self.table_repo.get_by_id(table_id)
        candidate = self.candidate_repo.get_by_id(candidate_id)
        result.table = TableModel(table)
        result.candidate = CandidateModel(candidate)
        # todo or do never XD validate fields
        return {
            "id": self.repo.save(result)
        }

    def update(self, id, data):
        result = ResultModel(data)
        self.repo.update(id, result)


    def delete(self, id):
        self.repo.delete(id)
