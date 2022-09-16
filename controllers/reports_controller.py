from db.reports_repository import ReportsRepository


class ReportsController():

    def __init__(self) -> None:
        self.repo = ReportsRepository()

    # obtener total de cada uno de los candidatos
    def get(self):
        return self.repo.reports()

    # obtener total de cada uno de los candidatos por mesa
    def get_by_table_id(self, args):
        return self.repo.reports_by_table_id(args["table"])

    # obtener total de votos por el id de candidato
    def get_by_candidate_id(self, args):
        return self.repo.reports_by_candidate_id(args['candidate'])

    # obtener total de un candidato en una mesa
    def get_by_table_candidate_id(self, args):
        return self.repo.reports_by_table_candidate_id(args['table'], args['candidate'])
