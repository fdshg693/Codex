import os
import sys


def launch_codex(prompt: str, args: str) -> str:
    """
    Codexを起動する関数。

    :param prompt: Codexに渡すプロンプト文字列
    :param args: コマンドライン引数
    """
    try:
        return f'codex {args} "{prompt}"'
    except Exception as e:
        print(f"Error launching Codex: {e}", file=sys.stderr)
        exit(1)


def create_codex_prompt() -> str:
    """
    Codexに渡すプロンプトを作成する。

    :return: Codexに渡すプロンプト文字列
    """
    prompt = "# Follow ./.codex/Agents.md to details.\n"
    return prompt


if __name__ == "__main__":
    # 引数を取得
    if len(sys.argv) != 0:
        args = " ".join(sys.argv[1:])
    else:
        args = ""

    # Codexに渡すプロンプトを作成
    prompt = create_codex_prompt()
    # Codexを起動
    code = launch_codex(prompt, args)
    # codeを返す
    print(code)
    sys.exit(0)
