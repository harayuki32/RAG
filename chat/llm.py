from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

# def generate_answer(client,prompt,llm_model):
#     # GPTで回答を生成
#     response = client.chat.completions.create(
#         # model="gpt-4o-mini",  # 最新推奨モデル（安価で高速）
#         model=llm_model,
#         messages=[
#             {"role": "system", "content": "あなたは与えられた情報をもとに質問に答えるアシスタントです。"},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.3
#     )

#     return response.choices[0].message.content


# ★追加：LangChainによる回答生成
def generate_answer(prompt, llm_model):
    # ① 回答生成に使用するモデルを準備
    llm = ChatGoogleGenerativeAI(
        model=llm_model,
        temperature=0.3
    )

    # ② Gemini APIにリクエストして回答を生成
    response = llm.invoke([
        SystemMessage(
            content="あなたは与えられた情報をもとに質問に答えるアシスタントです。"
        ),
        HumanMessage(content=prompt)
    ])

    # ③ 生成された回答を取り出す
    # return response.content

    # ★修正：回答テキストだけを返す
    return response.text


