from models.candidate_model import CandidateModel
from models.political_party_model import PoliticalPartyModel
from db.political_party_repository import PoliticalPartyRepository
from db.candidate_repository import CandidateRepository



class CandidateController():

    def __init__(self) -> None:
        self.repo = CandidateRepository()
        self.repo_political_party = PoliticalPartyRepository()

    def get_all(self, args):
        return list(self.repo.get_all())

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    # def get_by_document_id(self, document):
    #     pass

    # def get_by_resolution(self, resolution):
    #     pass

    def create(self, data, political_party_id):
        candidate = CandidateModel(data)
        political_party = self.repo_political_party.get_by_id(political_party_id)
        candidate.political_party = PoliticalPartyModel(political_party)
        return {
        "id": self.repo.save(candidate)
        }

    def update(self, id, data):
        candidate = CandidateModel(data)
        self.repo.update(id, candidate)


    def delete(self, id):
        self.repo.delete(id)
