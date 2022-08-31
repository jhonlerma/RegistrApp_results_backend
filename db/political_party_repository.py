from db.repository import Repository
from models.political_party_model import PoliticalPartyModel


class PoliticalPartyRepository(Repository[PoliticalPartyModel]):
    def __init__(self):
        super().__init__()
