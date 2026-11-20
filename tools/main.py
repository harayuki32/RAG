from pathlib import Path
from dotenv import load_dotenv
import argparse

# ★追加：LangChain版の処理
from tools.ingest import ingest_url
from database.embedding import create_embedding_model
from database.vector_store import load_vector_store
from database.retriever import find_relevant_chunks
from chat.prompt import create_prompt
from chat.llm import generate_answer


def rag_qa(url, question,provider):

    # ★追加：APIキーを読み込む
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(env_path)

    # ② 使用モデルを設定
    if provider == "gemini":
        # ★追加：Geminiで使用するモデル
        embedding_model = "gemini-embedding-001"
        llm_model = "gemini-3.1-flash-lite"

    elif provider == "openai":
        
        # ★追加：OpenAIで使用するモデル
        embedding_model = "text-embedding-3-small"
        llm_model = "gpt-4o-mini"
    else:
        raise ValueError(f"未対応のAPIです: {provider}")


    # ③ DBの設定
    db_name = "rag_documents"
    db_path = str(
        Path(__file__).resolve().parent.parent
        /"database" /"chroma_db"
    )



    # ⑤ Embeddingモデルを生成
    embeddings = create_embedding_model(embedding_model)


    # ⑥ 保存済みDBを読み込む
    vector_store = load_vector_store(
        embedding_model=embeddings,
        db_name=db_name,
        db_path= db_path
    )

    existing_data = vector_store.get(
        where={"source": url},
        limit=1,
        include=[]
    )

    print("データベースを読み込みました")

    if existing_data["ids"]:
       print("登録済みURLのため、DB作成を省略します")
    else:
        # ★修正：未登録のURLだけベクトル化・保存
        ingest_url(
            url=url,
            embedding_model=embedding_model,
            db_name=db_name,
            db_path=db_path
        )
        print("新しいURLをDBに保存しました")

    # ⑦ 関連Documentを検索
    relevant_chunks = find_relevant_chunks(
        question=question,
        vector_store=vector_store,
        k=3
    )

    print("関連するチャンクを検索しました")

    # ⑧ プロンプトを作成
    prompt = create_prompt(question, relevant_chunks)

    # ⑨ 回答を生成
    answer = generate_answer(
        prompt=prompt,
        llm_model=llm_model
    )

    return answer


# ★追加：main.pyを直接実行したときだけ動作
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--url", type=str, required=True)
    parser.add_argument("--question", type=str, required=True)
    parser.add_argument("--provider", type=str, required=True)

    args = parser.parse_args()

    answer = rag_qa(args.url, args.question, args.provider)

    print("生成された回答:",answer)