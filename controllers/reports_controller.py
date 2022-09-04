from models.table_model import TableModel
from models.candidate_model import CandidateModel
from models.political_party_model import PoliticalPartyModel
from models.reports_model import ReportsModel
from db.reports_repository import ReportsRepository
from db.table_repository import TableRepository
from db.candidate_repository import CandidateRepository
from db.political_party_repository import PoliticalPartyRepository



class ReportsController():

    def __init__(self) -> None:
        self.repo = ReportsRepository()

    def get(self): # obtener total de cada uno de los candidatos
        return self.repo.reports()

    def get_by_table_id(self, args): # obtener total de cada uno de los candidatos por mesa
        # print("\n-------------------------------------------------------------------")
        # print(args["table_id"])
        # print("-------------------------------------------------------------------\n")

        return self.repo.reports_by_table_id(args["table_id"])

    def get_by_candidate_id(self, args): # obtener total de votos por el id de candidato
        return self.repo.reports_by_candidate_id(args['candidate_id'])

    # def get_by_political_party_id(self, args): # obtener total de votos por el id de partido politico
    #     return self.repo.reports_by_political_party_id(args['political_party_id'])

    # def get_by_table_candidate_id(self, args): # obtener total de un candidato en una mesa
    #     return self.repo.reports_by_table_candidate_id(args['table_id'], args['candidate_id'])

    # def get_by_table_political_party_id(self, args): # obtener el total de un partido politico por mesa
    #     return self.repo.reports_by_table_political_party_id(args['table_id'], args['political_party_id'])

