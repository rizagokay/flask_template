from flask import (request, Blueprint, jsonify)

bp = Blueprint('api', __name__)

'''
    Write simple api methods here
'''

# POST Ping
@bp.route('/rest/ping', methods=["POST"])
@bp.route('/REST/Ping', methods=["POST"])
def ping():
    if request.is_json:
        return jsonify({"Message" : "Pong !"})
    else:
        return jsonify({'error' : "Request body must be JSON !"}), 400
