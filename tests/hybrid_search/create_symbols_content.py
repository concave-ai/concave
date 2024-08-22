import json
import os.path

workdir = "/Users/justwph/labs/hackathons/2024/playground/examples/pytest/4787fd64a4ca0dba5528b5651bddd254102fe9f3/src/"

cache = {}

with open('symbol_index.json') as f:
    rows = json.load(f)["data"]

results = []

for row in rows:
    byte_start = row["range"][4]
    byte_end = row["range"][5]
    file_path = os.path.join(workdir, row["file_path"])
    if file_path not in cache:
        with open(file_path) as f:
            cache[file_path] = f.read()
    content = cache[file_path][byte_start:byte_end]
    row["content"] = content
    results.append(row)


with open('symbol_index_with_content.json', 'w') as f:
    json.dump({"data": results}, f)
