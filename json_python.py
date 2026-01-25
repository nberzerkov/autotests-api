import json

json_data = """
{
  "name": "Никита",
  "age": 25,
  "is_student": false,
  "courses": ["Python", "QA Automation", "API Testing", {"name":  "Test"}],
  "address": {
    "city": "Москва",
    "zip-code": 284743,
    "ulitsa": {
      "name": "Быстринская"
    }
  }
}
"""

parsed_data = json.loads(json_data)

# print(type(parsed_data))
# print(parsed_data["courses"])

data = {
    "name": "Олег",
    "age": 30,
    "is_student": True
}

json_string = json.dumps(data, indent=4)
# print(json_string, type(json_string))


with open("json_example.json", "r", encoding="utf-8") as f:
    read_data = json.load(f)
    print(read_data, type(read_data))


with open("json_user.json", 'w', encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
