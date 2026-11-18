from langchain_chroma import Chroma

# ★追加：チャンクをベクトル化してChromaに保存
def create_vector_store(chunks, embedding_model, db_name, db_path):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        collection_name=db_name,
        persist_directory=db_path
    )

    return vector_store

# ★追加：保存済みChroma DBの読み込み
def load_vector_store(embedding_model, db_name, db_path):
    vector_store = Chroma(
        collection_name=db_name,
        embedding_function=embedding_model,
        persist_directory=db_path
    )

    return vector_store