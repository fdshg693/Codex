import subprocess
import select
import signal
import sys
import time


def run_with_watchdog(cmd, timeout=30):
    p = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,  # 行バッファリング
    )
    last_output = time.time()
    try:
        if p.stdout is None:
            raise RuntimeError("p.stdout is None. Cannot get file descriptor.")
        fd = p.stdout.fileno()
        while True:
            # 最大1秒待って、出力があれば読み出し
            rlist, _, _ = select.select([fd], [], [], 1.0)
            if rlist:
                line = p.stdout.readline()
                if not line:  # EOF
                    break
                sys.stdout.write(line)
                last_output = time.time()

            # プロセス終了をチェック
            if p.poll() is not None:
                break

            # タイムアウト判定
            if time.time() - last_output > timeout:
                print(
                    f"\n[{timeout}秒間出力なしのためSIGINTを送信します]",
                    file=sys.stderr,
                )
                p.send_signal(signal.SIGINT)
                try:
                    p.wait(5)  # SIGINT 後に5秒だけ待つ
                except subprocess.TimeoutExpired:
                    p.terminate()
                    p.wait()
                break
    finally:
        if p.stdout is not None:
            p.stdout.close()
        print("\n[プロセスが終了しました]", file=sys.stderr)


if __name__ == "__main__":
    # コマンドの組み立て例：末尾のドット（.）は不要です
    cmd = (
        './code_generate.sh --approval-mode full-auto "what is the capital of France?"'
    )
    run_with_watchdog(cmd, timeout=10)
