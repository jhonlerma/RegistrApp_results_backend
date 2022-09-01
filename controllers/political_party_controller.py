from models.political_party_model import PoliticalPartyModel
from db.political_party_repository import PoliticalPartyRepository


class PoliticalPartyController():

    def __init__(self) -> None:
        self.repo = PoliticalPartyRepository()

    def get_all(self, args):
        return list(self.repo.get_all())

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data):
        political_party = PoliticalPartyModel(data)
        # todo or do never XD validate fields
        return {
            "id": self.repo.save(political_party)
        }

    def update(self, id, data):
        political_party = PoliticalPartyModel(data)
        self.repo.update(id, political_party)


    def delete(self, id):
        self.repo.delete(id)
