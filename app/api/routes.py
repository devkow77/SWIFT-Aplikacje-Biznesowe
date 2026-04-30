from flask import Blueprint, request, jsonify
from app.services.swift_service import handle_swift_message

swift_bp = Blueprint("swift", __name__)

@swift_bp.route("/swift/message", methods=["POST"])
def receive_message():
    xml_data = request.data.decode("utf-8")
    result, status = handle_swift_message(xml_data)
    return jsonify(result), status