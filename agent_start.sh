# コードを生成させる
code_generate_prompt="You are a coding agent tasked with genereating code. Read and follow instructions written in .codex/CODING_AGENT.md to generate code"
./code_generate.sh --approval-mode full-auto  "$code_generate_prompt"

# コードを評価する
code_evaluate_prompt="You are a coding agent tasked with evaluating code. Read and follow instructions written in .codex/EVALUATING_AGENT.md to evaluate code and generate report"
./code_evaluate.sh --approval-mode full-auto "$code_evaluate_prompt"