from flask import jsonify, request, Blueprint
from controllers.political_party_controller import PoliticalPartyController
from decorators.logger_decorator import logger

political_party_module = Blueprint('political_party', __name__)
controller = PoliticalPartyController()


@political_party_module.get('/')
@logger
def get_political_parties():
    return jsonify(controller.get(request.args))


@political_party_module.post('/')
@logger
def create_political_party():
    return jsonify(controller.create(request.get_json())), 201


@political_party_module.get('/<string:id>')
def show_political_party(id):
    return jsonify(controller.get_by_id(id))


@political_party_module.put('/<string:id>')
def update_political_party(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204


@political_party_module.delete('/<string:id>')
def delete_political_party(id):
    controller.delete(id)
    return jsonify({}), 204
