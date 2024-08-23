from tree_sitter_tools.indexer.symbol_indexer import SymbolIndexer

if __name__ == "__main__":
    indexer = SymbolIndexer.from_dir("./")
    indexer.index()

