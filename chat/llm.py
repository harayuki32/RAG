def generate_answer(client,prompt,llm_model):
    # GPTで回答を生成
    response = client.chat.completions.create(
        # model="gpt-4o-mini",  # 最新推奨モデル（安価で高速）
        model=llm_model,
        messages=[
            {"role": "system", "content": "あなたは与えられた情報をもとに質問に答えるアシスタントです。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content