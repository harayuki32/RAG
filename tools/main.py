from database.chunker import split_into_chunks
from database.loader import get_webpage_text
from database.embedding import embed_text
from database.retriever import find_relevant_chunks
from database.vector_store import generate_answer
from pathlib import Path  # ★追加
from dotenv import load_dotenv  # ★追加
from openai import OpenAI  # ★追加

def rag_qa(url, question):

    # ★追加：APIキーを読み込む
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(env_path)

    # ★追加：OpenAIクライアントを生成
    client = OpenAI()

    """RAGを使った質問応答システムのメイン関数"""
    # 1. Webページからテキスト抽出
    text = get_webpage_text(url)
    print("Webページからテキストを抽出しました")

    # 2. テキストをチャンクに分割
    chunks = split_into_chunks(text)
    print(f"テキストを{len(chunks)}個のチャンクに分割しました")

    # 3. チャンクをベクトル化
    chunk_embeddings = []
    for chunk in chunks:
        embedding = embed_text(client,chunk)
        chunk_embeddings.append({
            "text": chunk,
            "embedding": embedding
        })
    print("チャンクをベクトル化しました")

    # 4. 関連チャンクを見つける
    relevant_chunks = find_relevant_chunks(question, chunk_embeddings,client)
    print("質問に関連するチャンクを見つけました")

    # 5. 回答を生成
    answer = generate_answer(question, relevant_chunks,client)
    print("回答を生成しました")

    return answer
