import json
import subprocess


class FullTextSearcher():

    def __init__(self, work_dir):
        self.work_dir = work_dir

    def cmd(self, keys: list[str]):
        args = [f"-e '{t}'" for t in keys]
        return f"rg --json -n -w {' '.join(args)} --glob '*.py' {self.work_dir}"

    def parse(self, rows):
        results = {
        }

        for row in rows:

            if row['type'] != 'match':
                continue
            file = [
            ]
            path = row['data']['path']['text']
            for m in row['data']['submatches']:
                file.append({
                    "line": row['data']['line_number'],
                    "content": row['data']['lines']['text'],
                })
            if path not in results:
                results[path] = []
            results[path].extend(file)
        return results

    def search(self, keys: list[str]):
        cmd = self.cmd(keys)
        cmd_out = subprocess.run(["sh", "-c", cmd], stdout=subprocess.PIPE)
        raw = cmd_out.stdout.decode('utf-8')
        rows = [json.loads(l) for l in raw.split('\n') if l]
        return self.parse(rows)

    def print(self, results):
        for path, files in results.items():
            relative_path = path.replace(self.work_dir, "")
            print(relative_path)
            for file in files:
                line = str(file['line']).rjust(5, ' ')
                print(f"{line} | {file['content'].rstrip()}")
            print()
