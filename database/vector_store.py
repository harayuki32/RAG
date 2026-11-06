import numpy as np
from embedding import embed_text

def cosine_similarity(vec1, vec2):
    """コサイン類似度を計算する関数"""
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

def find_relevant_chunks(question, chunk_embeddings,client,top_k=2):
    """質問に関連するチャンクを見つける関数"""
    # 質問をベクトル化
    question_embedding = embed_text(client,question)

    # 各チャンクとの類似度を計算
    similarities = []
    for i, chunk_data in enumerate(chunk_embeddings):
        similarity = cosine_similarity(question_embedding, chunk_data["embedding"])
        similarities.append({
            "index": i,
            "similarity": similarity,
            "text": chunk_data["text"]
        })

    # 類似度の高い順にソート
    similarities.sort(key=lambda x: x["similarity"], reverse=True)

    # 上位k個を返す
    return similarities[:top_k]