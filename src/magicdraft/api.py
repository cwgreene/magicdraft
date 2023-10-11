import uuid
import os
import uuid

from flask import Blueprint, request

from .shared.draft import Draft, DraftResponse

API = Blueprint('api', __name__)

draft_db = {}

UNAUTHORIZED = ("Unauthorized", 401)

@API.route("/api/draft", methods=["POST"])
def post_draft():
    draft_id = uuid.uuid4()
    seed = os.urandom(8)
    draft = Draft(draft_id, seed)
    draft_db[draft_id] = draft
    name = request.json["name"]
    draft.players.append(name)
    return  {
                "version": "1",
                "draft": draft.to_dict()
            }

@API.route("/api/draft/<id>", methods=["GET"])
def get_draft(id):
    id = uuid.UUID(id)
    if id not in draft_db:
        return UNAUTHORIZED
    return  {
                "version" : "1",
                "draft": draft_db[id].to_dict()
            }

@API.route("/api/draft/<id>/join", methods=["POST"])
def join_draft(id):
    id = uuid.UUID(id)
    if id not in draft_db:
        return UNAUTHORIZED
    draft = draft_db[id]
    # TODO: Add Check on max players
    # TODO: Check name isn't used
    newPlayer = request.json["name"]
    draft.players.append(newPlayer)

    return DraftResponse(draft).to_dict()