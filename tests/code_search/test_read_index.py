import json
import time

from internal.codebase.search.read_index import read_scip
from internal.codebase.vector.vector import VectorIndexer, VectorSearcher


class File:
    def __init__(self, relative_path: str):
        self.path = f"/tmp/testlab/pytest/{relative_path}"
        with open(self.path, "r") as f:
            self.raw = f.read()
        self.lines = self.raw.splitlines()

    def read(self, range: list[int]):
        if len(range) == 3:
            start_line, start_char, end_char = range
            return self.lines[start_line][start_char:end_char]
        if len(range) == 4:
            start_line, start_char, end_line, end_char = range
            first_line = self.lines[start_line][start_char:]
            middle_lines = self.lines[start_line + 1:end_line]
            last_line = self.lines[end_line][:end_char]
            return "\n".join([first_line] + middle_lines + [last_line])

        return "WRONG RANGE"


def create_vector_index():
    p = read_scip("./index.scip")

    n = time.time()
    indexer = VectorIndexer(f"vector-{n}")
    # docs = []

    for doc in p.documents:
        for o in doc.occurrences:
            if o.enclosing_range:
                # print("=====================================")
                # print(doc.relative_path, o.symbol)
                # print(File(doc.relative_path).read(o.enclosing_range))
                content = f"{o.symbol}\n{doc.relative_path}\n"
                content += File(doc.relative_path).read(o.enclosing_range)
                indexer.add_document(content, {"symbol": o.symbol})
                # docs.append({"text": content, "metadata": {"symbol": o.symbol}})

    print("start indexing...")
    indexer.commit()


def test_search():
    searcher = VectorSearcher("vector-1723406760.0007172")
    query = "where define --runxfail"
    results = searcher.search(query)
    for i, node in enumerate(results.nodes):
        print(f"{i + 1}.  {results.similarities[i]} {node.metadata['symbol']}")


if __name__ == "__main__":
    test_search()
