from flask import jsonify, request, Blueprint
from controllers.result_controller import ResultController

result_module = Blueprint('result', __name__)
controller = ResultController()


@result_module.get('/list')
def get_results():
    return jsonify(controller.get(request.args))


@result_module.post('/')
def create_result():
    return jsonify(controller.create(request.get_json())), 201


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
