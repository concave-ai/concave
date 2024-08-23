import argparse
import os.path

from concave.internal.codebase.search.symbol.searcher import SymbolSearcher

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Symbol search")
    parser.add_argument('--keywords', type=str, nargs='+', help='Keywords to search for')

    if not os.path.exists("./symbol_index.parquet"):
        raise FileNotFoundError("symbol_index.parquet not found")

    indexer = SymbolSearcher("./symbol_index.parquet")

    args = parser.parse_args()
    print(indexer.search(args.keywords))

