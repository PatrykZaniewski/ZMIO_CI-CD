from flask import Blueprint, request

from service.integral_service import calculate_integral_by_rectangle_rule

integral_blueprint = Blueprint("integral", __name__, url_prefix="/integral")


@integral_blueprint.route("")
def calculate_integral_result():
    args = request.args

    a = float(args.get("a", 0))
    b = float(args.get("b", 0))
    rectangle_number = float(args.get("rectangle_number", 1))

    return str(calculate_integral_by_rectangle_rule(a, b, rectangle_number))
