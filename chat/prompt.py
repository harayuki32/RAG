def create_prompt(question, relevant_chunks):
    """質問と関連チャンクからプロンプトを作成する"""

    """関連チャンクをもとに回答を生成する関数"""
    # プロンプトの作成
    context = "\n\n".join([chunk["text"] for chunk in relevant_chunks])
    prompt = f"""以下は、Webページから抽出された情報です：

    {context}

    上記の情報をもとに、次の質問に答えてください：
    {question}

    できるだけ与えられた情報のみを使って回答してください。情報が不足している場合は、「提供された情報からは回答できません」と答えてください。"""


    return prompt