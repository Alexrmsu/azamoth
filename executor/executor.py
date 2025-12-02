import json
import zendriver

from typing import List

def read_instructions(json_payload) -> None | List:
    get_instructions = json.loads(json_payload).get('instructions', None)
    return get_instructions
