from models.candidate_model import CandidateModel
from db.candidate_repository import CandidateRepository

class CandidateController():

    def __init__(self) -> None:
        self.repo = CandidateRepository()

    def get(self, args):
        pass

    def get_by_id(self, id):
        pass

    def create(self, data):
        pass

    def update(self, id, data):
        pass

    def delete(self, id):
        pass

