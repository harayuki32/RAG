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