from flask import jsonify, request, Blueprint
from controllers.result_controller import ResultController

result_module = Blueprint('result', __name__)
controller = ResultController()


@result_module.get('/list')
def get_results():
    return jsonify(controller.get_all(request.args))


@result_module.post('/table_id/<string:table_id>/candidate_id/<String:candidate_id>')
def create_result(table_id, candidate_id):
    return jsonify(controller.create(request.get_json(), table_id, candidate_id))


@result_module.get('/<string:id>')
def show_result(id):
    return jsonify(controller.get_by_id(id))


@result_module.put('/<string:id>')
def update_result(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204


@result_module.delete('/<string:id>')
def delete_result(id):
    controller.delete(id)
    return jsonify({}), 204
