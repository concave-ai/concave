import json
import os

from concave.internal.codebase.search.vector.vector_indexer import VectorIndexer

TIDB_PASSWORD = os.environ.get("TIDB_PASSWORD", "")
TIDB_USER = os.environ.get("TIDB_USER", "")

TIDB_DATABASE_URL = f"mysql+pymysql://{TIDB_USER}.root:{TIDB_PASSWORD}@gateway01.us-west-2.prod.aws.tidbcloud.com:4000/test?ssl_ca=/etc/ssl/cert.pem&ssl_verify_cert=false&ssl_verify_identity=false"

if __name__ == "__main__":
    with open("symbol_index_with_content.json") as f:
        symbols = json.load(f)["data"]



    index = VectorIndexer(
        tidb_connection_url=TIDB_DATABASE_URL,
        table_name="pytest_20240821"
    )

    for s in symbols:
        index.add_document(s["content"], metadata={
            "_id": s["id"],
            "kine": s["kind"],
        })

    index.commit()
