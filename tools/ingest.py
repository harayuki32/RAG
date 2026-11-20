#ベクトル保存
from pathlib import Path

from database.loader import get_webpage_text
from database.chunker import split_into_chunks
from database.embedding import create_embedding_model
from database.vector_store import create_vector_store


# ★追加：URLからベクトルDBを作成する
def ingest_url(url, embedding_model, db_name, db_path):

    # ① Webページを取得
    docs = get_webpage_text(url)

    # ② チャンク分割
    chunks = split_into_chunks(docs)

    # ③ Embeddingモデルを生成
    embeddings = create_embedding_model(embedding_model)
    

    # ④ ベクトル化してDBに保存
    vector_store = create_vector_store(
        chunks=chunks,
        embedding_model=embeddings,
        db_name=db_name,
        db_path=db_path
    )

    return vector_store