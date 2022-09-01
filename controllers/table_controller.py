from models.table_model import TableModel
from db.table_repository import TableRepository


class TableController():

    def __init__(self) -> None:
        self.repo = TableRepository()

    def get_all(self, args):
        return list(self.repo.get_all())

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data):
        table = TableModel(data)
        # todo or do never XD validate fields
        return {
            "id": self.repo.save(table)
        }

    def update(self, id, data):
        table = TableModel(data)
        self.repo.update(id, table)


    def delete(self, id):
        self.repo.delete(id)
