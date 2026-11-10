def generate_answer(question, relevant_chunks,client):
    """関連チャンクをもとに回答を生成する関数"""
    # プロンプトの作成
    context = "\n\n".join([chunk["text"] for chunk in relevant_chunks])
    prompt = f"""以下は、Webページから抽出された情報です：

{context}

上記の情報をもとに、次の質問に答えてください：
{question}

できるだけ与えられた情報のみを使って回答してください。情報が不足している場合は、「提供された情報からは回答できません」と答えてください。"""

    # GPTで回答を生成
    response = client.chat.completions.create(
        # model="gpt-4o-mini",  # 最新推奨モデル（安価で高速）
        model="gemini-3.1-flash-lite",
        messages=[
            {"role": "system", "content": "あなたは与えられた情報をもとに質問に答えるアシスタントです。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content