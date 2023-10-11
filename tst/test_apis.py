from magicdraft import create_app
from magicdraft.shared.draft import Draft, DraftResponse

def test_draft_creation():
    app = create_app({"TESTING": True})
    client = app.test_client()
    res = client.post("/api/draft", json= {
        "name": "myName",
    })
    draft = DraftResponse.from_dict(res.json).draft

    res2 = client.get(f"/api/draft/{draft.uuid}")
    draft2 = Draft.from_dict(res2.json["draft"])
    assert draft.uuid == draft2.uuid
    assert "myName" in draft2.players

def test_join_draft():
    app = create_app({"TESTING": True})
    client = app.test_client()
    res = client.post("/api/draft", json={"name": "bob"})
    res = DraftResponse.from_dict(res.json)
    draft = res.draft
    id = draft.uuid
    res = DraftResponse.from_dict(client.post(f"/api/draft/{id}/join", json={"name": "joe"}).json)
    draft = res.draft
    assert set(["bob","joe"]) == set(draft.players)