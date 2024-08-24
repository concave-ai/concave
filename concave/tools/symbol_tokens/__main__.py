import os.path

from concave.internal.codebase.search.symbol.searcher import SymbolSearcher

if __name__ == "__main__":
    if not os.path.exists("./symbol_index.parquet"):
        raise FileNotFoundError("symbol_index.parquet not found")

    indexer = SymbolSearcher("./symbol_index.parquet")
    print(indexer.tokens())

