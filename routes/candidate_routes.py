from flask import jsonify, request, Blueprint
from controllers.candidate_controller import CandidateController
from decorators.logger_decorator import logger

candidate_module = Blueprint('candidate', __name__)
controller = CandidateController()


@candidate_module.get('/')
@logger
def get_candidates():
    return jsonify(controller.get(request.args))


@candidate_module.post('/')
@logger
def create_candidate():
    return jsonify(controller.create(request.get_json())), 201


@candidate_module.get('/<string:id>')
def show_candidate(id):
    return jsonify(controller.get_by_id(id))


@candidate_module.put('/<string:id>')
def update_candidate(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204


@candidate_module.delete('/<string:id>')
def delete_candidate(id):
    controller.delete(id)
    return jsonify({}), 204
