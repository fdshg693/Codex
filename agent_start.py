from run_with_watchdog import run_with_watchdog
import subprocess
import sys

if __name__ == "__main__":
    print("マネージャーエージェントを起動します")
    cmd = r"""
manager_prompt="You are a manager of agents. You will manage agents to generate and evaluate code. Read and follow instructions written in .codex/MANAGER_AGENT.md to manage agents"
./project_manager.sh --approval-mode full-auto "$manager_prompt"
"""
    run_with_watchdog(cmd, timeout=30)
    print("\nマネージャーエージェントが終了しました")

    # managerの作成したタスクをエージェントが使用するディレクトリにコピー
    print("[タスクのテンプレートを更新します]")
    cmd = r"""
cp manager/current_task.yaml template/.codex/task.yaml
"""
    p = subprocess.run(cmd, shell=True, check=True)
    # プロセスを終了
    if p.returncode != 0:
        print("タスクのテンプレートの更新に失敗しました", file=sys.stderr)
        exit(1)
    print("[タスクのテンプレートを更新しました]")

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
