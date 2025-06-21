# Move into the working directory
cd runs || exit 1

# Find existing run_N directories
shopt -s nullglob
run_dirs=(run_[0-9]*)
shopt -u nullglob

if [ ${#run_dirs[@]} -eq 0 ]; then
  echo "There are 0 runs."
  exit 1
else
  # get the maximum run number
  max_run_number=0
  for d in "${run_dirs[@]}"; do
    [[ "$d" =~ ^run_([0-9]+)$ ]] && (( ${BASH_REMATCH[1]} > max_run_number )) && max_run_number=${BASH_REMATCH[1]}
  done
fi

# activate the virtual environment if it exists
if [ -d "../.venv" ]; then
  source ../.venv/bin/activate
  echo "Activated virtual environment."
else
  echo "No virtual environment found. Skipping activation."
fi

# Create the evalluate directory if it doesn't exist
mkdir -p "../evaluate/run_$max_run_number"

# copy only python files and directories in run_N to evaluate/run_N (macOS compatible)
cd "run_$max_run_number"
find . -name '*.py' -exec bash -c '
  for f; do
    dir=$(dirname "$f")
    mkdir -p "../../evaluate/run_'$max_run_number'/$dir"
    cp "$f" "../../evaluate/run_'$max_run_number'/$f"
  done
' bash {} +
cd ..

# Add .codex directory to evaluate/run_N
rsync -av --ignore-existing "run_$max_run_number/.codex/" "../evaluate/run_$max_run_number/.codex/"

# 作業ディレクトリに移動
cd "../evaluate/run_$max_run_number"

# 受け取った引数をCODEXコマンドにそのまま渡す
CODEX "$@"

