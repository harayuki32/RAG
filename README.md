# RAG
こちらのGitでは、RAGの実装及び運用を想定して開発を行う。

## ディレクトリ構成

```text
RAG/
├── README.md
├── run.sh
├── requirements.txt
│
├── base_notebook/
│   └── RAG実装.ipynb
│
├── chat/
│   ├── prompt.py
│   └── llm.py
│
├── database/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedding.py
│   ├── retriever.py
│   └── vector_store.py
│
└── tools/
    ├── main.py
    └── ingest.py
```

## 環境構築
Pythonの仮想環境を構築し、必要なライブラリ群をそろえる。
```text
python -m venv {.venv}
.\{.venv}\Scripts\activate
pip install -r requirements.txt
```