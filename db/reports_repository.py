from db.repository import Repository
from models.result_model import ResultModel
from bson import ObjectId

class ReportsRepository(Repository[ResultModel]):
    def __init__(self):
        super().__init__()

    def reports(self):  # obtener total de cada uno de los candidatos
        filter = {}

    # obtener total de cada uno de los candidatos por mesa
    def reports_by_table_id(self, table_id):
        filter = {"table.$id": ObjectId(table_id)}
        data = self.query(filter)
        result = {}
        for d in data:
            if "table" not in result:
                result['table'] = d['table']['numero']
                result['_id'] = d['table']['_id']
                result['results'] = {}
            if d['candidate']['name'] + " " + d['candidate']['last_name'] not in result['results']:
                result['results'].update({d['candidate']['name'] + " " + d['candidate']['last_name'] : 1})
            else:
                result['results'][d['candidate']['name'] + " " + d['candidate']['last_name']] += 1

        return result


    # obtener total de votos por el id de candidato
    def reports_by_candidate_id(self, candidate_id):
        filter = {}


    # obtener total de un candidato en una mesa
    def reports_by_table_candidate_id(self, table_id, candidate_id):
        filter = {
            "$and": [
                {},
                {}
            ]
        }
