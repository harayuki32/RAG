def embed_text(client,text):
    """テキストをベクトル化する関数"""

    response = client.embeddings.create(
    model="text-embedding-3-small",  # 旧adaより高性能＆安価
    input=text
    )

    return response.data[0].embedding
