from csv import DictReader
from files import JSON_FILE_PATH
from files import CSV_FILE_PATH
import json

with open(JSON_FILE_PATH, "r") as f:
    users = json.loads(f.read())
    users_list = []
    for i in users:
        users_list.append(
            {"name": i["name"], "gender": i["gender"], "address": i["address"], "age": i["age"], "books": []}
        )

with open(CSV_FILE_PATH, newline='') as f:
    reader = DictReader(f)
    books = []
    for row in reader:
        books.append({"title": row["Title"], "author": row["Author"], "pages": row["Pages"], "genre": row["Genre"]})

while len(books) > 0:
    for user in users_list:
        if len(books) > 0:
            user['books'].append(books.pop())

    with open('result.json', 'w') as r:
        result = json.dumps(users_list, indent=4)
        r.write(result)
