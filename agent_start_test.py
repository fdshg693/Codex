from run_with_watchdog import run_with_watchdog
import subprocess
import sys

if __name__ == "__main__":
    print("マネージャーエージェントを起動します")
    cmd = r"""
manager_prompt="What is 1+1?"
./project_manager.sh --approval-mode full-auto "$manager_prompt"
"""
    run_with_watchdog(cmd, timeout=10)
    print("\nマネージャーエージェントが終了しました")

    # manager/current_task.yamlをtemplate/task.yamlにコピー
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
code_generate_prompt="What is 1+1?"
./code_generate.sh --approval-mode full-auto  "$code_generate_prompt"
"""
    run_with_watchdog(cmd, timeout=10)

    print("\n[コーディングエージェントが終了しました]")

    print("[コード評価エージェントを起動します]")
    cmd = r"""
code_evaluate_prompt="What is 1+1?"
./code_evaluate.sh --approval-mode full-auto  "$code_evaluate_prompt"
"""
    run_with_watchdog(cmd, timeout=10)

    print("\n[コード評価エージェントが終了しました]")
    print("[エージェントの実行が完了しました]")
