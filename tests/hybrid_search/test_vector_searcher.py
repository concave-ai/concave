import json
import os

from concave.internal.codebase.search.vector.vector import VectorSearcher
from concave.internal.codebase.search.vector.vector_indexer import VectorIndexer

TIDB_PASSWORD = os.environ.get("TIDB_PASSWORD", "")
TIDB_USER = os.environ.get("TIDB_USER", "")

TIDB_DATABASE_URL = f"mysql+pymysql://{TIDB_USER}.root:{TIDB_PASSWORD}@gateway01.us-west-2.prod.aws.tidbcloud.com:4000/test?ssl_ca=/etc/ssl/cert.pem&ssl_verify_cert=false&ssl_verify_identity=false"

if __name__ == "__main__":
    print("connecting to tidb...")
    searcher = VectorSearcher(
        tidb_connection_url=TIDB_DATABASE_URL,
        table_name="pytest-0823"
    )

    results = searcher.search("code relative 'EncodedFile'", top_k=6)
    results.print()



