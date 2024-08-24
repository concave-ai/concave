import os.path

from concave.internal.codebase.search.symbol.searcher import SymbolSearcher
from concave.internal.codebase.search.vector.vector_indexer import VectorIndexer

workdir = "./"
def get_symbols():
    if not os.path.exists(os.path.join(workdir, "symbol_index.parquet")):
        raise FileNotFoundError("symbol_index.parquet not found")
    cache = {}
    searcher = SymbolSearcher(os.path.join(workdir, "symbol_index.parquet"))
    symbols = searcher.all_symbols()
    for row in symbols:
        byte_start = row.byte_range[0]
        byte_end = row.byte_range[1]
        file_path = os.path.join(workdir, row.file_path)
        if file_path not in cache:
            with open(file_path) as f:
                cache[file_path] = f.read()

        content = cache[file_path][byte_start:byte_end]
        row.content = content
    return symbols


if __name__ == "__main__":
    symbols = get_symbols()
    TIDB_PASSWORD = os.environ.get("TIDB_CLOUD_PASSWORD", "")
    TIDB_USER = os.environ.get("TIDB_CLOUD_USER", "")
    TIDB_TABLE = os.environ.get("TIDB_CLOUD_TABLE", "")

    TIDB_DATABASE_URL = f"mysql+pymysql://{TIDB_USER}.root:{TIDB_PASSWORD}@gateway01.us-west-2.prod.aws.tidbcloud.com:4000/test?ssl_ca=/etc/ssl/cert.pem&ssl_verify_cert=false&ssl_verify_identity=false"


    index = VectorIndexer(
        tidb_connection_url=TIDB_DATABASE_URL,
        table_name=TIDB_TABLE
    )

    for s in symbols:
        index.add_document(s.content, metadata={
            "_id": s.id,
            "kine": s.kind,
        })

    print("Indexing...")
    index.commit()
    print("Indexing done")




