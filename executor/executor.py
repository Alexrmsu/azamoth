import json

from typing import List

def read_instructions(json_payload) -> None | List:
    get_instructions = json.loads(json_payload).get('instructions', None)
    return get_instructions



if __name__ == "__main__":
    instructive: list[dict] = [
        {"hola": "mundo", "instructions": [
            {"command": "print('Hello World!')"}
        ]}
    ]
    final = []
    for i in instructive:
        x = read_instructions()
        final.append(x)
    print(final)