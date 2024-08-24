import pyarrow.parquet as pq
from pydantic import BaseModel


class SearchResult(BaseModel):
    id: str
    kind: str
    range: list[int]
    file_path: str
    content: str =""

    @property
    def byte_range(self) -> tuple[int, int]:
        return self.range[-2], self.range[-1]


class SymbolSearcher:
    def __init__(self, index_path):
        self.table = pq.read_table(index_path)

    def tokens(self):
        tokens = set()
        ids = self.table.column('id')
        for i in ids:
            parts = i.as_py().split('.')
            tokens.update(parts)
        return tokens

    def all_symbols(self):
        ids = self.table.column('id').to_pylist()
        kinds = self.table.column('kind').to_pylist()
        ranges = self.table.column('range').to_pylist()
        file_paths = self.table.column('file_path').to_pylist()

        return [
            SearchResult(
                id=id_value,
                kind=kind_value,
                range=range_value,
                file_path=relative_path_value
            )
            for id_value, kind_value, range_value, relative_path_value in zip(ids, kinds, ranges, file_paths)
        ]

    def search(self, keywords: list[str]) -> list[SearchResult]:
        indexes = []
        ids = self.table.column('id')
        for i, id_value in enumerate(ids):
            id_str = id_value.as_py()
            if any(keyword in id_str for keyword in keywords):
                indexes.append(i)

        result = []
        for i in indexes:
            id_value = ids[i]
            kind_value = self.table.column('kind')[i]
            range_value = self.table.column('range')[i]
            relative_path_value = self.table.column('file_path')[i]

            result.append(SearchResult(
                id=id_value.as_py(),
                kind=kind_value.as_py(),
                range=range_value.as_py(),
                file_path=relative_path_value.as_py()
            ))
        return result
