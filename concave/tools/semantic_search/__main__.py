import argparse
import os.path

from concave.internal.codebase.search.symbol.searcher import SymbolSearcher
from concave.internal.codebase.search.vector.vector import VectorSearcher

TIDB_PASSWORD = os.environ.get("TIDB_CLOUD_PASSWORD", "")
TIDB_USER = os.environ.get("TIDB_CLOUD_USER", "")
TIDB_TABLE = os.environ.get("TIDB_CLOUD_TABLE", "")

TIDB_DATABASE_URL = f"mysql+pymysql://{TIDB_USER}.root:{TIDB_PASSWORD}@gateway01.us-west-2.prod.aws.tidbcloud.com:4000/test?ssl_ca=/etc/ssl/cert.pem&ssl_verify_cert=false&ssl_verify_identity=false"

# python -m concave.tools.semantic_search --question "How to create a new table in MySQL?" --top_k 5
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Semantic search")
    parser.add_argument("--question", type=str, help="The question to search for")
    parser.add_argument("--top_k", type=int, default=5, help="The number of results to return")

    if not os.path.exists("./symbol_index.parquet"):
        raise FileNotFoundError("symbol_index.parquet not found")

    indexer = SymbolSearcher("./symbol_index.parquet")

    args = parser.parse_args()
    searcher = VectorSearcher(
        tidb_connection_url=TIDB_DATABASE_URL,
        table_name=TIDB_TABLE
    )

    results = searcher.search(args.question, top_k=args.top_k)
    results.print()

