"""Header Data Functions"""
import setup  # pylint: disable=unused-import, wrong-import-order
from flask import request
from flask import jsonify
from flask_restful import Resource

class HeaderData(Resource):
    """Header Data Functions"""
    def get(self):
        """Displays User IP and referrer"""
        response = jsonify(
            {
                "ip": request.environ["HTTP_X_FORWARDED_FOR"],
                "referrer": request.environ["HTTP_REFERER"],
            }
        )
        response.access_control_allow_origin = "*"
        return response
