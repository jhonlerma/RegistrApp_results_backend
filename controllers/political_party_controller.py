from models.political_party_model import PoliticalPartyModel
from db.political_party_repository import PoliticalPartyRepository

class PoliticalPartyController():

    def __init__(self) -> None:
        self.repo = PoliticalPartyRepository()

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
