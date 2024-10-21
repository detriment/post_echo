import json

from icecream import ic

with open("log.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    try:
        ic(json.loads(line)["status"])
    except json.JSONDecodeError:
        ic(line)
