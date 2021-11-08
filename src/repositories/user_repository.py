import json

from typing import List, Dict


def get_users() -> List[Dict[str, any]]:
    with open("./files/users.json", "r+", encoding="utf-8") as f:
        users = json.loads(f.read())
        return users
