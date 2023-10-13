import json
import os

js = json.load(open("./data/AllPrintings.json"))
for s in js["data"]:
    with open(f"./data/sets/{s}.json", "w") as setfile:
        setfile.write(json.dumps(s))
