import json
import os

def load_json(rel_path: str):
    """
    rel_path is relative to repo root (for example: 'data/create_user_payload.json')
    """
    root = os.path.join(os.path.dirname(__file__), '..')
    full = os.path.normpath(os.path.join(root, rel_path))
    with open(full, 'r', encoding='utf-8') as fh:
        return json.load(fh)
