import json
import os
from bson import json_util # pip install bson


def writeAJson(data, name: str):
  try:
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./json"):
        os.makedirs("./json")
        

    with open(f"./json/{name}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))
    print(f"JSON {name} criado com sucesso!")
  except Exception as e:
    print(e)