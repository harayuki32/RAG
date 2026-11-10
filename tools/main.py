from database.chunker import split_into_chunks
from database.loader import get_webpage_text
from database.embedding import embed_text
from database.retriever import generate_answer 
from database.vector_store import find_relevant_chunks
from pathlib import Path  # ★追加
from dotenv import load_dotenv  # ★追加
from openai import OpenAI  # ★追加
import os

def rag_qa(url, question):

    # ★追加：APIキーを読み込む
    env_path = Path(__file__).resolve().parent.parent / ".env"

    load_dotenv(env_path)

    provider = "gemini"

    if provider == "gemini":
        # ★追加：Gemini APIに接続する
        client = OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

        # ★追加：Geminiで使用するモデル
        embedding_model = "gemini-embedding-001"
        llm_model = "gemini-3.1-flash-lite"

    elif provider == "openai":
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        # ★追加：OpenAIで使用するモデル
        embedding_model = "text-embedding-3-small"
        llm_model = "gpt-4o-mini"

    else:
        raise ValueError(f"未対応のAPIです: {provider}")



    print("OpenAIクライアントの生成成功")


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
        embedding = embed_text(client,chunk,embedding_model)
        chunk_embeddings.append({
            "text": chunk,
            "embedding": embedding
        })
    print("チャンクをベクトル化しました")

    # 4. 関連チャンクを見つける
    relevant_chunks = find_relevant_chunks(question, chunk_embeddings,client,embedding_model)
    print("質問に関連するチャンクを見つけました")

    # 5. 回答を生成
    answer = generate_answer(question, relevant_chunks,client,llm_model)
    print("回答を生成しました")

    return answer

# ★追加：main.pyを直接実行したときだけ動作
if __name__ == "__main__":

    url = "https://example.com"
    question = "このWebページについて教えてください"

    answer = rag_qa(url, question)

    print(answer)