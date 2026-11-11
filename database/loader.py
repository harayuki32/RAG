import requests
from bs4 import BeautifulSoup

def get_webpage_text(url):
    """指定されたURLのWebページからテキストを抽出する関数"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 不要なタグを除去
    for tag in soup(['script', 'style', 'header', 'footer', 'nav']):
        tag.decompose()

    # テキストを取得して整形
    text = soup.get_text()
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    text = ' '.join(lines)

    return text