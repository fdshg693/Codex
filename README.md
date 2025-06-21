# CODEXを使ったコード生成実験


## コード編集エージェントの起動
    - ./agent_start.sh 

### コードを生成させる
./code_generate.sh --approval-mode full-auto "Read .codex/CODING_AGENTS.md File"
### コードを評価する
./code_evaluate.sh



## フォルダ構成
- `template/` - コード変更を行う作業ディレクトリ
    - `template/.codex/` - Codexの設定ファイルやリソース
- `user-only/` - ユーザ固有の設定やメモ
- `run/` - コード生成エージェントの作業ディレクトリ
- `evaluate/` - コード評価エージェントの作業ディレクトリ