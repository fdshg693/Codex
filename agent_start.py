from run_with_watchdog import run_with_watchdog

if __name__ == "__main__":
    print("[コーディングエージェントを起動します]")
    cmd = r"""
code_generate_prompt="You are a coding agent tasked with genereating code. Read and follow instructions written in .codex/CODING_AGENT.md to generate code"
./code_generate.sh --approval-mode full-auto  "$code_generate_prompt"
"""
    run_with_watchdog(cmd, timeout=30)

    print("\n[コーディングエージェントが終了しました]")

    print("[コード評価エージェントを起動します]")
    cmd = r"""
code_evaluate_prompt="You are a code evaluation agent tasked with evaluating code. Read and follow instructions written in .codex/CODE_EVALUATION_AGENT.md to evaluate code"
./code_evaluate.sh --approval-mode full-auto  "$code_evaluate_prompt"
"""
    run_with_watchdog(cmd, timeout=30)

    print("\n[コード評価エージェントが終了しました]")
    print("[エージェントの実行が完了しました]")
