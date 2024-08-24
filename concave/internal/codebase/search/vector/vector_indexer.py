import os

from llama_index.core import Document
from llama_index.core.ingestion import IngestionPipeline, DocstoreStrategy
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.embeddings.voyageai import VoyageEmbedding
from llama_index.vector_stores.tidbvector import TiDBVectorStore


class VectorIndexer:
    documents = []

    def __init__(self, tidb_connection_url, table_name):
        self._vector_store = TiDBVectorStore(
            connection_string=tidb_connection_url,
            table_name=table_name,
            distance_strategy="cosine",
            vector_dimension=1536,
            drop_existing_table=False,
        )
        self._docstore = SimpleDocumentStore()

        if "VOYAGE_API_KEY" not in os.environ:
            raise ValueError(
                "VOYAGE_API_KEY environment variable is not set. Please set it to your Voyage API key."
            )

        self._embed_model = VoyageEmbedding(
            model_name="voyage-code-2",
            voyage_api_key=os.environ.get("VOYAGE_API_KEY"),
            truncation=True,
            embed_batch_size=128,
        )

        self.embed_pipeline = IngestionPipeline(
            transformations=[self._embed_model],
            docstore_strategy=DocstoreStrategy.UPSERTS_AND_DELETE,
            docstore=self._docstore,
            vector_store=self._vector_store,
        )

    def add_document(self, text, metadata=None):
        self.documents.append(Document(
            text=text,
            mimetypes="text/x-python",
            metadata=metadata,
        ))

    def commit(self, show_progress=False):
        self.embed_pipeline.run(show_progress=show_progress, documents=self.documents, num_workers=1)
        self.documents = []
