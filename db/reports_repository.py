from typing import Counter
from db.repository import Repository
from models.result_model import ResultModel
from bson import ObjectId
from  collections import Counter


class ReportsRepository(Repository[ResultModel]):
    def __init__(self):
        super().__init__()

    # obtener total de cada uno de los candidatos
    def reports(self):  
        data = self.get_all()
        candidate_list = []
        candidate_list_to = []
        result = []
        for d in data:
            candidate_name = {'candidate': d['candidate']['name'] + " " + d['candidate']['last_name']}
            candidate_list.append(candidate_name)

        for candidate in candidate_list:
            if candidate not in candidate_list_to:
                result.append({'candidate': candidate['candidate'], 'votes': candidate_list.count(candidate)})
                candidate_list_to.append(candidate)
        
        return result

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
                result['results'].update(
                    {d['candidate']['name'] + " " + d['candidate']['last_name']: 1})
            else:
                result['results'][d['candidate']['name'] + " " + d['candidate']['last_name']] += 1

        return result

    # obtener total de votos por el id de candidato
    def reports_by_candidate_id(self, candidate_id):
        filter = {"candidate.$id": ObjectId(candidate_id)}
        data = self.query(filter)
        result = {}
        for d in data:
            if d['candidate']['name'] + " " + d['candidate']['last_name'] not in result:
                result.update({d['candidate']['name'] + " " + d['candidate']['last_name']: 1})
            else:
                result[d['candidate']['name'] + " " + d['candidate']['last_name']] += 1

        return result

    # obtener total de un candidato en una mesa
    def reports_by_table_candidate_id(self, table_id, candidate_id):
        filter = {
            "$and": [
                {"candidate.$id": ObjectId(candidate_id)},
                {"table.$id": ObjectId(table_id)}
            ]
        }
        data = self.query(filter)
        result = {}
        for d in data:
            if "table" not in result:
                result['table'] = d['table']['numero']
                result['_id'] = d['table']['_id']
                result['results'] = {}
            if d['candidate']['name'] + " " + d['candidate']['last_name'] not in result['results']:
                result['results'].update({d['candidate']['name'] + " " + d['candidate']['last_name']: 1})
            else:
                result['results'][d['candidate']['name'] + " " + d['candidate']['last_name']] += 1

        return result
