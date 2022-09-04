from flask import jsonify, request, Blueprint
from controllers.reports_controller import ReportsController

reports_module = Blueprint('reports', __name__)
controller = ReportsController()


@reports_module.get('/')
def get_results():
    return jsonify(controller.get())

@reports_module.get('/by_table')
def get_reports_by_table():
    return jsonify(controller.get_by_table_id(request.args.to_dict()))

@reports_module.get('/by_candidate')
def get_reports_by_candidate():
    return jsonify(controller.get_by_candidate_id(request.args.to_dict()))

@reports_module.get('/by_political_party')
def get_reports_by_political_party():
    return jsonify(controller.get_by_political_party_id(request.args.to_dict()))

@reports_module.get('/by_table_candidate')
def get_reports_by_table_candidate():
    return jsonify(controller.get_by_table_candidate_id(request.args.to_dict()))

@reports_module.get('/by_table_political_party')
def get_reports_by_table_political_party():
    return jsonify(controller.get_by_table_political_party_id(request.args.to_dict()))

    # def get():
    #     pass

    # def get_by_table_id():
    #     pass

    # def get_tolal_by_candidate_id():
    #     pass

    # def get_by_political_party_id():
    #     pass

    # def get_by_table_candidate_id():
    #     pass

    # def get_by_table_political_party_id():
    #     pass
