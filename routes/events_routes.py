from flask import Blueprint, jsonify, request
from controllers.events_controller import get_events, get_event_by_id

events_bp = Blueprint("events", __name__)


@events_bp.route("/api/events", methods=["GET"])
def fetch_events():
    return jsonify(get_events()), 200

@events_bp.route("/api/events/<event_id>", methods=["GET"])
def fetch_event_by_id(event_id):

    # 1. Validate integer
    if not event_id.isdigit():
        return jsonify({"message": "Bad request"}), 400

    event = get_event_by_id(int(event_id))

    # 2. Not found
    if event is None:
        return jsonify({"message": "Not found"}), 404

    return jsonify({"event": event}), 200