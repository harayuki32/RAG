import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader


# def get_webpage_text(url):
#     """指定されたURLのWebページからテキストを抽出する関数"""
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # 不要なタグを除去
#     for tag in soup(['script', 'style', 'header', 'footer', 'nav']):
#         tag.decompose()

#     # テキストを取得して整形
#     text = soup.get_text()
#     lines = [line.strip() for line in text.split('\n') if line.strip()]
#     text = ' '.join(lines)

#     return text

# ★追加：LangChainによるWebページ取得

def get_webpage_text(url):
    """指定されたURLのWebページからテキストを抽出する関数"""
    loader = WebBaseLoader(
        web_path=url,
        raise_for_status = True
    )

    # soup = loader.scrape()

    # for tag in soup(["script","style","header","footer","nav"]):
    #     tag.docompose()

    # text = soup.get_text()
    # lines = [line.strip() for line in text.split("\n") if line.strip()]
    # text = " ".join(lines)


    # return [Document(page_content = text,metadate = {"source":url})]

    docs = loader.load()

    return docs
