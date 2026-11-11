while true
do
    echo "================================"
    echo "       RAG Application"
    echo "================================"
    echo "1. データベース作成"
    echo "2. RAGによる質問応答"
    echo "3. 終了"
    echo ""
    read -p "選択してください：" choice

    case $choice in

        1)
            echo ""
            read -p "データベースに追加したいURLを入力してください：" url

            echo ""
            echo "データベースを作成します..."
            python tools/ingest.py --url "$url"
            ;;

        2)
            echo ""
            read -p "LLMに渡したい情報のURLを入力してください：" url

            read -p "質問文を入力してください：" question

            read -p "利用したいLLM（gemini, openai）を入力してください：" provider

            echo ""
            echo "入力された質問：$question"
            echo "回答に使用するLLM：$provider"
            echo "回答を生成しています..."

            # ★修正：モジュールとして実行
            python -m tools.main \
                --url "$url" \
                --question "$question" \
                --provider "$provider"
            ;;

        3)
            echo "終了します。"
            break
            ;;

        *)
            echo "無効な選択です。再入力してください。"
            ;;
    esac
done