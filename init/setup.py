import os
import sys
from pathlib import Path


def launch_codex(prompt: str):
    """
    Codexを起動する関数。

    :param prompt: Codexに渡すプロンプト文字列
    """
    try:
        print("Launching Codex with prompt:", prompt)
        os.system(f'codex "{prompt}"')
    except Exception as e:
        print(f"Error launching Codex: {e}", file=sys.stderr)


def read_task_yaml(task_yaml_path: Path) -> str:
    import yaml

    try:
        with open(task_yaml_path, "r", encoding="utf-8") as f:
            task = yaml.safe_load(f)
        description = task.get("description", "")
    except Exception as e:
        # throw an error if the file cannot be read
        print(f"Error reading task.yaml: {e}", file=sys.stderr)
        exit(1)
    return description


def read_agents_md(agents_md_path: Path) -> str:
    """
    AGENTS.mdの内容を読み込み、プロンプトに付加する。

    :param agents_md_path: AGENTS.mdファイルのパス（デフォルト: "AGENTS.md"）
    :return: AGENTS.mdの内容を付加した新しいプロンプト文字列
    """
    try:
        with open(agents_md_path, "r", encoding="utf-8") as f:
            agents_content = f.read()
        return agents_content
    except FileNotFoundError:
        print(f"Error: {agents_md_path} not found.", file=sys.stderr)
        exit(1)


def create_codex_prompt(description: str, agents_md: str) -> str:
    """
    Codexに渡すプロンプトを作成する。

    :param description: タスクの説明
    :param agents_md: AGENTS.mdの内容
    :return: Codexに渡すプロンプト文字列
    """
    prompt = f"# Codex Prompt\n\n"
    prompt += f"## Agents.md\n{agents_md}\n\n"
    prompt += f"## Task Description\n{description}\n\n"
    return prompt


if __name__ == "__main__":
    # コマンドライン引数からtask.yamlのパスを取得
    if len(sys.argv) > 1:
        task_yaml_path_relative = sys.argv[1]
    else:
        task_yaml_path_relative = "../task.yaml"

    # task.yamlを読み込み、タスクの説明を取得
    task_yaml_path_absolute = Path(__file__).resolve().parent / task_yaml_path_relative
    description = read_task_yaml(task_yaml_path_absolute)
    # AGENTS.mdを読み込み、内容を取得
    agents_md_path = Path(__file__).resolve().parent / "../.codex/AGENTS.md"
    agents_md = read_agents_md(agents_md_path)
    # Codexに渡すプロンプトを作成
    prompt = create_codex_prompt(description, agents_md)
    # Codexを起動
    launch_codex(prompt)
