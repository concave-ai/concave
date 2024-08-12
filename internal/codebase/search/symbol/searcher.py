import os

from sqlmodel import Session, create_engine, select

from internal.codebase.search.symbol.db import SymbolInfo, Occurrences


class SymbolsResponse:

    def __init__(self, symbols, occurrences):
        self.symbols = symbols
        self.occurrences = occurrences

    def print(self):
        print("=" * 30)
        print("| SYMBOLS SEARCH RESULTS")
        print(f"| Found {len(self.symbols)} symbols and {len(self.occurrences)} occurrences")
        print("=" * 30)
        print("Symbols:")
        for symbol in self.symbols:
            print(f"{symbol.symbol}")
            print("-" * 30)
            print(f"{symbol.documentation}")
            print()
        print("Occurrences:")
        for occurrence in self.occurrences:
            print(
                f"  {occurrence.role} in {occurrence.filename} at {occurrence.start_line}:{occurrence.start_char}-{occurrence.end_line}:{occurrence.end_char}")


class SymbolSearcher:

    def __init__(self, index_path: str):
        index_file = os.path.join(index_path, "scip.sqlite")
        if not os.path.exists(index_file):
            raise FileNotFoundError(f"Index file {index_file} does not exist")

        self.engine = create_engine(f"sqlite:///{index_file}")

    def search(self, query: str):
        with Session(self.engine) as session:
            symbol_query = select(SymbolInfo).where(SymbolInfo.symbol.like(f"%{query}%"))
            symbols_exec = session.exec(symbol_query)
            symbols = symbols_exec.all()

            occurrences_query = select(Occurrences).where(Occurrences.symbol.like(f"%{query}%"))
            occurrences_exec = session.exec(occurrences_query)
            occurrences = occurrences_exec.all()

            return SymbolsResponse(symbols, occurrences)
