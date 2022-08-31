from models.candidate_model import CandidateModel
from db.candidate_repository import CandidateRepository


class CandidateController():

    def __init__(self) -> None:
        self.repo = CandidateRepository()

    def get_all(self, args):
        return list(self.repo.get_all())

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    # def get_by_document_id(self, document):
    #     pass

    # def get_by_resolution(self, resolution):
    #     pass

    def create(self, data):
        candidate = CandidateModel(data)
        # todo or do never XD validate fields
        return {
            "id": self.repo.save(candidate)
        }

    def update(self, id, data):
        candidate = CandidateModel(data)
        self.repo.update(id, candidate)


    def delete(self, id):
        self.repo.delete(id)
