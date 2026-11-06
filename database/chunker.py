def split_into_chunks(text, chunk_size=1000, overlap=100):
    """テキストを指定サイズのチャンクに分割する関数"""
    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))

        # 文の途中で切れないように調整
        if end < len(text):
            # 最後の空白を見つける
            while end > start and text[end] != ' ':
                end -= 1
            if end == start:  # 空白が見つからなかった場合
                end = min(start + chunk_size, len(text))

        print(f"start={start}, end={end}, next_start={max(end - overlap, start + 1)}")  # デバッグ用

        # チャンクを追加
        chunks.append(text[start:end])

        if end == len(text):   # 末尾まで行ったら終了
            break
        # 次のチャンクの開始位置（オーバーラップあり）
        start = max(end - overlap, start + 1)

    return chunks
