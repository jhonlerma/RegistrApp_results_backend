from models.table_model import TableModel
from db.table_repository import TableRepository

class TableController():

    def __init__(self) -> None:
        self.repo = TableRepository()

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
