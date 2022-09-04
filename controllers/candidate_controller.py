from models.candidate_model import CandidateModel
from models.political_party_model import PoliticalPartyModel
from db.political_party_repository import PoliticalPartyRepository
from db.candidate_repository import CandidateRepository



class CandidateController():

    def __init__(self) -> None:
        self.repo = CandidateRepository()
        self.political_party_repo = PoliticalPartyRepository()

    def get_all(self, args):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def get_by_document_id(self, document):
        return self.repo.get_one_by_key("document", document)

    def get_by_resolution(self, resolution):
        return self.repo.get_one_by_key("resolution", resolution)

    def create(self, data, political_party_id):
        candidate = CandidateModel(data)
        political_party = self.political_party_repo.get_by_id(political_party_id)
        candidate.political_party = PoliticalPartyModel(political_party)
        return {
        "id": self.repo.save(candidate)
        }

    def update(self, id, data):
        candidate = CandidateModel(data)
        self.repo.update(id, candidate)


    def delete(self, id):
        self.repo.delete(id)
