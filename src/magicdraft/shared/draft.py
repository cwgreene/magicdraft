import random
import json
import base64

class Draft():
    KEYS = ["uuid", "seed", "players", "originalPacks", "started", "playerSelections", "playerPacks"]

    def __init__(self, id, seed):
        self.uuid = id
        self.seed = seed
        self.players = []
        self.originalPacks = []
        self.started = False

        # TODO: max players

        # mutable
        self.playerSelections = {}
        self.playerPacks = {}

        self.rnd = random.Random(seed)

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "seed": base64.b64encode(self.seed).decode(),
            "players": self.players,
            "originalPacks": self.originalPacks,
            "started": self.started,
            "playerSelections": self.playerSelections,
            "playerPacks": self.playerPacks
        }

    @staticmethod
    def from_dict(d):
        draft = Draft(d["uuid"], d["seed"])
        for key in Draft.KEYS:
            setattr(draft, key, d[key])
        return draft
    
class DraftRequest():
    def __init__(self, name):
        self.name = name
        self.version = "1"
    
    def to_json(self):
        return json.dumps(self.__dict__)

class DraftResponse():
    def __init__(self, draft=None, version="1"):
        self.version = version
        self.draft = draft

    @staticmethod
    def from_dict(d):
        resp = DraftResponse()
        resp.version = d["version"]
        resp.draft = Draft.from_dict(d["draft"])
        return resp
    
    def to_dict(self):
        return {"version": self.version, "draft": self.draft.to_dict()}
