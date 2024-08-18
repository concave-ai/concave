from concave.internal.codebase.search.symbol.searcher import SymbolSearcher

with open("./index.scip", "rb") as f:
    index = f.read()

searcher = SymbolSearcher(index)
symbols = searcher.all_src_symbols()
print(len(symbols))
tokens = searcher.all_src_tokens()
print(len(tokens))
for i in tokens:
    print(i)