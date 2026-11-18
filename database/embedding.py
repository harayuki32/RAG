from langchain_google_genai import GoogleGenerativeAIEmbeddings

# def embed_text(client,text):
#     """テキストをベクトル化する関数"""

#     response = client.embeddings.create(
#     model="text-embedding-3-small",  # 旧adaより高性能＆安価
#     input=text
#     )

#     return response.data[0].embedding

# ★追加：LangChain用Embeddingモデルの生成
def create_embedding_model(model_name):
    embeddings = GoogleGenerativeAIEmbeddings(
        model=model_name
    )

    return embeddings