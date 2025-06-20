import os
import shutil
from pathlib import Path


def copy_files(src_dir, dst_dir):
    """
    src_dir内のすべてのファイルをdst_dirにコピーする
    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dst_file = os.path.join(dst_dir, filename)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)


if __name__ == "__main__":

    root_dir = Path(__file__).parent.parent
    src_directories = root_dir / "runs"
    # src_directoriesの中から最新のディレクトリを取得
    src_directory = max(src_directories.iterdir(), key=os.path.getmtime)
    # コピー先のディレクトリ
    dst_directory = root_dir / "template"

    # ファイルをコピー
    copy_files(str(src_directory), str(dst_directory))
    print(f"Files copied from {src_directory} to {dst_directory}")

    # ファイルをコピー
    copy_files(src_directory, dst_directory)
    print(f"Files copied from {src_directory} to {dst_directory}")
