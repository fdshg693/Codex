# CODEXを使ったコード生成実験


## コード編集エージェントの起動
    - ```python
    python3 agent_start.py
    ```    

### コードを生成させる
```bash
code_generate_prompt="You are a coding agent tasked with genereating code. Read and follow instructions written in .codex/CODING_AGENT.md to generate code"
./code_generate.sh --approval-mode full-auto  "$code_generate_prompt"
```
### コードを評価する
```bash
code_evaluate_prompt="You are a code evaluation agent tasked with evaluating code. Read and follow instructions written in .codex/CODE_EVALUATION_AGENT.md to evaluate code"
./code_evaluate.sh --approval-mode full-auto  "$code_evaluate_prompt"
```


## フォルダ構成
- `template/` - コード変更を行う作業ディレクトリ
    - `template/.codex/` - Codexの設定ファイルやリソース
    - `template/.codex/resource/` - コード生成や評価に必要なリソース
        - `python_coding_style.md` - Pythonのコーディングスタイルガイド
        - `CODING_AGENT.md` - コード生成エージェントの指示
        - `CODE_EVALUATION_AGENT.md` - コード評価エージェントの指示
        - `template/.codex/output/` - コード生成エージェントの出力ディレクトリ
- `user-only/` - ユーザ固有の設定やメモ
- `run/` - コード生成エージェントの作業ディレクトリ
- `evaluate/` - コード評価エージェントの作業ディレクトリ